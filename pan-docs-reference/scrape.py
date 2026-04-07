#!/usr/bin/env python3
"""PAN Docs Reference Scraper — downloads Palo Alto Networks documentation
pages and converts them to searchable local markdown files.

Usage:
    python3 scrape.py init --urls-file FILE --project NAME
    python3 scrape.py add URL [--project NAME] [--tags tag1,tag2]
    python3 scrape.py fetch [--force] [--url URL]
    python3 scrape.py list [--project NAME]
    python3 scrape.py index
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

SCRIPT_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = SCRIPT_DIR / "manifest.json"
DOCS_DIR = SCRIPT_DIR / "docs"
INDEX_PATH = SCRIPT_DIR / "index.md"
LOG_PATH = SCRIPT_DIR / "scrape.log"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_PATH, mode="a"),
    ],
)
log = logging.getLogger("scrape")


# ── Manifest helpers ────────────────────────────────────────────────────

def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {"version": 1, "last_updated": None, "sources": []}


def save_manifest(manifest: dict):
    manifest["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)


def normalize_url(url: str) -> str:
    """Strip fragment and trailing slash for dedup."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def url_to_local_path(url: str) -> str:
    """Convert a PAN docs URL to a local relative path under docs/.

    Example: https://docs.paloaltonetworks.com/vm-series/11-1/vm-series-deployment/bootstrap-the-vm-series-firewall
    becomes: docs/vm-series/11-1/bootstrap-the-vm-series-firewall.md
    """
    parsed = urlparse(url)
    parts = [p for p in parsed.path.strip("/").split("/") if p]
    if not parts:
        return "docs/unknown.md"

    # Strategy: keep product (parts[0]), version if present (parts[1] if matches version pattern),
    # and the leaf filename. This keeps the tree shallow.
    product = parts[0]
    leaf = parts[-1]

    # Check if second segment looks like a version (e.g., "11-1", "10-2")
    version = None
    if len(parts) > 1 and re.match(r"^\d+[-\.]\d+", parts[1]):
        version = parts[1]

    if version:
        return f"docs/{product}/{version}/{leaf}.md"
    elif len(parts) > 1:
        # Use product/section/leaf for non-versioned paths
        section = parts[1]
        return f"docs/{product}/{section}/{leaf}.md"
    else:
        return f"docs/{product}/{leaf}.md"


def find_entry(manifest: dict, url: str) -> dict | None:
    norm = normalize_url(url)
    for entry in manifest["sources"]:
        if normalize_url(entry["url"]) == norm:
            return entry
    return None


# ── HTML to Markdown converter ──────────────────────────────────────────

class PanDocsConverter(HTMLParser):
    """Converts PAN docs HTML to clean markdown."""

    SKIP_TAGS = {"script", "style", "svg", "noscript", "iframe", "nav", "footer"}
    BLOCK_TAGS = {"p", "div", "section", "article", "main", "header", "li", "tr", "blockquote"}

    def __init__(self):
        super().__init__()
        self.output: list[str] = []
        self.skip_depth = 0
        self.tag_stack: list[str] = []
        self.in_pre = False
        self.in_code = False
        self.in_table = False
        self.table_rows: list[list[str]] = []
        self.current_row: list[str] = []
        self.current_cell: list[str] = []
        self.is_header_row = False
        self.list_stack: list[str] = []  # 'ul' or 'ol'
        self.list_counters: list[int] = []
        self.link_href: str | None = None
        self.link_text: list[str] = []
        self.in_link = False
        self.heading_level = 0
        self.heading_text: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag_lower = tag.lower()

        # Skip certain tags entirely
        if tag_lower in self.SKIP_TAGS:
            self.skip_depth += 1
            return

        if self.skip_depth > 0:
            return

        # Skip feedback, related-links, and other boilerplate divs
        if tag_lower == "div":
            cls = attrs_dict.get("class", "")
            if any(skip in cls for skip in ["feedback", "related-links", "cookie", "modal", "overlay"]):
                self.skip_depth += 1
                return

        self.tag_stack.append(tag_lower)

        # Headings
        if tag_lower in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading_level = int(tag_lower[1])
            self.heading_text = []

        # Links
        elif tag_lower == "a":
            href = attrs_dict.get("href", "")
            if href and not href.startswith("#") and not href.startswith("javascript:"):
                self.in_link = True
                self.link_href = href
                self.link_text = []

        # Lists
        elif tag_lower in ("ul", "ol"):
            self.list_stack.append(tag_lower)
            self.list_counters.append(0)

        elif tag_lower == "li":
            if self.list_stack:
                indent = "  " * (len(self.list_stack) - 1)
                if self.list_stack[-1] == "ol":
                    self.list_counters[-1] += 1
                    self.output.append(f"\n{indent}{self.list_counters[-1]}. ")
                else:
                    self.output.append(f"\n{indent}- ")

        # Code
        elif tag_lower == "pre":
            self.in_pre = True
            self.output.append("\n```\n")

        elif tag_lower == "code" and not self.in_pre:
            self.in_code = True
            self.output.append("`")

        # Tables
        elif tag_lower == "table":
            self.in_table = True
            self.table_rows = []

        elif tag_lower == "tr":
            self.current_row = []
            self.is_header_row = False

        elif tag_lower in ("td", "th"):
            self.current_cell = []
            if tag_lower == "th":
                self.is_header_row = True

        # Bold / italic
        elif tag_lower in ("strong", "b"):
            self.output.append("**")

        elif tag_lower in ("em", "i"):
            self.output.append("*")

        # Line break
        elif tag_lower == "br":
            self.output.append("\n")

        # Horizontal rule
        elif tag_lower == "hr":
            self.output.append("\n---\n")

        # Images
        elif tag_lower == "img":
            alt = attrs_dict.get("alt", "")
            src = attrs_dict.get("src", "")
            if alt or src:
                self.output.append(f"![{alt}]({src})")

    def handle_endtag(self, tag):
        tag_lower = tag.lower()

        if tag_lower in self.SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return

        if self.skip_depth > 0:
            # Check if this is a div closing a skipped section
            if tag_lower == "div":
                self.skip_depth = max(0, self.skip_depth - 1)
            return

        if self.tag_stack and self.tag_stack[-1] == tag_lower:
            self.tag_stack.pop()

        # Headings
        if tag_lower in ("h1", "h2", "h3", "h4", "h5", "h6") and self.heading_level:
            text = "".join(self.heading_text).strip()
            if text:
                self.output.append(f"\n\n{'#' * self.heading_level} {text}\n\n")
            self.heading_level = 0
            self.heading_text = []

        # Links
        elif tag_lower == "a" and self.in_link:
            text = "".join(self.link_text).strip()
            if text and self.link_href:
                self.output.append(f"[{text}]({self.link_href})")
            elif text:
                self.output.append(text)
            self.in_link = False
            self.link_href = None
            self.link_text = []

        # Lists
        elif tag_lower in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            if self.list_counters:
                self.list_counters.pop()
            self.output.append("\n")

        # Code
        elif tag_lower == "pre":
            self.in_pre = False
            self.output.append("\n```\n")

        elif tag_lower == "code" and not self.in_pre:
            self.in_code = False
            self.output.append("`")

        # Tables
        elif tag_lower in ("td", "th"):
            cell_text = "".join(self.current_cell).strip()
            cell_text = cell_text.replace("|", "\\|")  # escape pipes in cell content
            self.current_row.append(cell_text)

        elif tag_lower == "tr":
            if self.current_row:
                self.table_rows.append((self.is_header_row, self.current_row))

        elif tag_lower == "table":
            self._flush_table()
            self.in_table = False

        # Bold / italic
        elif tag_lower in ("strong", "b"):
            self.output.append("**")

        elif tag_lower in ("em", "i"):
            self.output.append("*")

        # Block-level elements get paragraph breaks
        elif tag_lower in ("p", "div", "section", "blockquote"):
            self.output.append("\n\n")

    def handle_data(self, data):
        if self.skip_depth > 0:
            return

        # Route text to the right accumulator
        if self.heading_level:
            self.heading_text.append(data)
        elif self.in_link:
            self.link_text.append(data)
        elif self.in_table and self.current_cell is not None:
            self.current_cell.append(data)
        elif self.in_pre:
            self.output.append(data)
        else:
            # Collapse whitespace for non-pre content
            text = re.sub(r"[ \t]+", " ", data)
            self.output.append(text)

    def _flush_table(self):
        if not self.table_rows:
            return
        # Determine column count
        max_cols = max(len(row) for _, row in self.table_rows)
        if max_cols == 0:
            return

        self.output.append("\n\n")

        first_is_header, first_row = self.table_rows[0]
        # Pad rows to max_cols
        padded_first = first_row + [""] * (max_cols - len(first_row))
        self.output.append("| " + " | ".join(padded_first) + " |\n")
        self.output.append("| " + " | ".join(["---"] * max_cols) + " |\n")

        for i, (is_header, row) in enumerate(self.table_rows):
            if i == 0:
                continue
            padded = row + [""] * (max_cols - len(row))
            self.output.append("| " + " | ".join(padded) + " |\n")

        self.output.append("\n")

    def get_markdown(self) -> str:
        text = "".join(self.output)
        # Clean up excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Strip leading/trailing whitespace
        text = text.strip()
        return text


def extract_content_html(html: str) -> str:
    """Extract the main content area from a PAN docs page."""
    # Try to find the DITA topic content div
    patterns = [
        r'<div[^>]*class="[^"]*topic[^"]*"[^>]*>(.*)',
        r'<div[^>]*class="[^"]*content-body[^"]*"[^>]*>(.*)',
        r'<main[^>]*>(.*)</main>',
        r'<article[^>]*>(.*)</article>',
    ]
    for pattern in patterns:
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if match:
            content = match.group(1)
            # Truncate at feedback/footer sections
            for cutoff in ['<div class="feedback', '<footer', '<div class="related-links-container',
                           '<div class="cookie', '<div id="usabilla']:
                idx = content.find(cutoff)
                if idx != -1:
                    content = content[:idx]
            return content

    # Fallback: try to get body content
    body_match = re.search(r"<body[^>]*>(.*)</body>", html, re.DOTALL | re.IGNORECASE)
    if body_match:
        return body_match.group(1)

    return html


def extract_title(html: str) -> str:
    """Extract page title from HTML."""
    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        # Remove common suffixes
        for suffix in [" - Palo Alto Networks", " | Palo Alto Networks", " - TechDocs"]:
            if title.endswith(suffix):
                title = title[: -len(suffix)]
        return title.strip()
    return ""


def html_to_markdown(html: str) -> str:
    """Convert HTML content to markdown."""
    content = extract_content_html(html)
    converter = PanDocsConverter()
    converter.feed(content)
    return converter.get_markdown()


# ── Fetch logic ─────────────────────────────────────────────────────────

def fetch_url(url: str) -> str | None:
    """Fetch a URL and return HTML content, or None on failure."""
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=30) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            return resp.read().decode(charset)
    except (HTTPError, URLError, TimeoutError) as e:
        log.error(f"Failed to fetch {url}: {e}")
        return None


def fetch_entry(entry: dict, force: bool = False) -> bool:
    """Fetch and convert a single manifest entry. Returns True on success."""
    url = entry["url"]
    local_path = SCRIPT_DIR / entry["local_path"]

    log.info(f"Fetching: {url}")

    html = fetch_url(url)
    if html is None:
        entry["status"] = "fetch_error"
        return False

    title = extract_title(html) or entry.get("title", "")
    markdown = html_to_markdown(html)

    if not markdown or len(markdown) < 50:
        log.warning(f"Conversion produced very little content for {url}")
        entry["status"] = "conversion_warning"
        # Still save what we got

    # Content hash for change detection
    content_hash = hashlib.sha256(markdown.encode()).hexdigest()[:16]

    # Check if content changed (skip write if identical and not forced)
    if not force and local_path.exists() and entry.get("content_hash") == content_hash:
        log.info(f"  No changes detected, skipping: {local_path.name}")
        return True

    # Build output with metadata header
    now = datetime.now(timezone.utc).isoformat()
    header = (
        f"<!-- Source: {url} -->\n"
        f"<!-- Fetched: {now} -->\n"
        f"<!-- Project: {entry.get('project', '')} -->\n"
        f"<!-- Tags: {', '.join(entry.get('tags', []))} -->\n\n"
    )

    # Ensure the title is in the markdown
    if title and not markdown.startswith(f"# {title}"):
        full_content = f"{header}# {title}\n\n{markdown}"
    else:
        full_content = f"{header}{markdown}"

    # Write file
    local_path.parent.mkdir(parents=True, exist_ok=True)
    with open(local_path, "w") as f:
        f.write(full_content)

    # Update entry
    entry["title"] = title
    entry["status"] = "ok"
    entry["last_fetched"] = now
    entry["content_hash"] = content_hash

    log.info(f"  Saved: {local_path} ({len(markdown)} chars)")
    return True


# ── CLI commands ────────────────────────────────────────────────────────

def cmd_init(args):
    """Import URLs from a file into the manifest."""
    manifest = load_manifest()

    urls_file = Path(args.urls_file)
    if not urls_file.exists():
        log.error(f"File not found: {urls_file}")
        sys.exit(1)

    added = 0
    with open(urls_file) as f:
        for line in f:
            line = line.strip()
            if not line or not line.startswith("http"):
                continue

            url = normalize_url(line)
            if find_entry(manifest, url):
                log.info(f"  Already in manifest: {url}")
                continue

            local_path = url_to_local_path(url)
            entry = {
                "url": url,
                "project": args.project or "",
                "tags": [],
                "local_path": local_path,
                "title": "",
                "status": "pending",
                "last_fetched": None,
                "content_hash": None,
            }
            manifest["sources"].append(entry)
            added += 1
            log.info(f"  Added: {url}")

    save_manifest(manifest)
    log.info(f"Imported {added} new URLs from {urls_file}")


def cmd_add(args):
    """Add a single URL to the manifest."""
    manifest = load_manifest()
    url = normalize_url(args.url)

    if find_entry(manifest, url):
        log.info(f"Already in manifest: {url}")
        return

    tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
    local_path = url_to_local_path(url)

    entry = {
        "url": url,
        "project": args.project or "",
        "tags": tags,
        "local_path": local_path,
        "title": "",
        "status": "pending",
        "last_fetched": None,
        "content_hash": None,
    }
    manifest["sources"].append(entry)
    save_manifest(manifest)
    log.info(f"Added: {url} -> {local_path}")


def cmd_fetch(args):
    """Fetch all or a specific URL."""
    manifest = load_manifest()

    if args.url:
        entry = find_entry(manifest, args.url)
        if not entry:
            log.error(f"URL not in manifest: {args.url}")
            sys.exit(1)
        fetch_entry(entry, force=args.force)
    else:
        total = len(manifest["sources"])
        success = 0
        for i, entry in enumerate(manifest["sources"], 1):
            if not args.force and entry.get("status") == "ok" and entry.get("last_fetched"):
                log.info(f"[{i}/{total}] Skipping (already fetched): {entry['url']}")
                success += 1
                continue
            log.info(f"[{i}/{total}] Processing...")
            if fetch_entry(entry, force=args.force):
                success += 1
        log.info(f"Fetch complete: {success}/{total} successful")

    save_manifest(manifest)


def cmd_list(args):
    """List manifest entries."""
    manifest = load_manifest()

    entries = manifest["sources"]
    if args.project:
        entries = [e for e in entries if e.get("project") == args.project]

    if not entries:
        print("No entries found.")
        return

    for entry in sorted(entries, key=lambda e: e.get("local_path", "")):
        status = entry.get("status", "?")
        title = entry.get("title", "") or "(no title)"
        project = entry.get("project", "")
        status_icon = {"ok": "+", "pending": ".", "fetch_error": "X", "conversion_warning": "!"}.get(status, "?")
        print(f"  [{status_icon}] {title}")
        print(f"      URL: {entry['url']}")
        print(f"      Path: {entry.get('local_path', '?')}  Project: {project}")
        print()


def cmd_index(args=None):
    """Generate index.md from manifest."""
    manifest = load_manifest()

    # Group by product (first directory under docs/)
    groups: dict[str, list[dict]] = {}
    for entry in manifest["sources"]:
        if entry.get("status") not in ("ok", "conversion_warning"):
            continue
        path = entry.get("local_path", "")
        parts = path.split("/")
        product = parts[1] if len(parts) > 1 else "other"
        groups.setdefault(product, []).append(entry)

    lines = [
        "# PAN Docs Reference Index\n",
        f"*Auto-generated on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}*\n",
        f"*{len(manifest['sources'])} total sources tracked*\n\n",
    ]

    for product in sorted(groups):
        lines.append(f"## {product.replace('-', ' ').title()}\n\n")
        for entry in sorted(groups[product], key=lambda e: e.get("title", "")):
            title = entry.get("title", "") or entry["url"].split("/")[-1]
            local = entry.get("local_path", "")
            project = entry.get("project", "")
            tags = ", ".join(entry.get("tags", []))
            tag_str = f" `[{tags}]`" if tags else ""
            project_str = f" ({project})" if project else ""
            lines.append(f"- [{title}]({local}){project_str}{tag_str}\n")
            lines.append(f"  Source: {entry['url']}\n")
        lines.append("\n")

    with open(INDEX_PATH, "w") as f:
        f.writelines(lines)

    log.info(f"Index written to {INDEX_PATH}")


# ── Main ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="PAN Docs Reference Scraper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    p_init = subparsers.add_parser("init", help="Import URLs from a file")
    p_init.add_argument("--urls-file", required=True, help="Path to file containing URLs")
    p_init.add_argument("--project", default="", help="Project tag (e.g., c-bootstrapping)")

    # add
    p_add = subparsers.add_parser("add", help="Add a single URL")
    p_add.add_argument("url", help="URL to add")
    p_add.add_argument("--project", default="", help="Project tag")
    p_add.add_argument("--tags", default="", help="Comma-separated tags")

    # fetch
    p_fetch = subparsers.add_parser("fetch", help="Fetch and convert pages")
    p_fetch.add_argument("--force", action="store_true", help="Re-fetch all pages")
    p_fetch.add_argument("--url", default=None, help="Fetch a specific URL only")

    # list
    p_list = subparsers.add_parser("list", help="List manifest entries")
    p_list.add_argument("--project", default=None, help="Filter by project")

    # index
    subparsers.add_parser("index", help="Regenerate index.md")

    args = parser.parse_args()

    if args.command == "init":
        cmd_init(args)
    elif args.command == "add":
        cmd_add(args)
    elif args.command == "fetch":
        cmd_fetch(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "index":
        cmd_index(args)


if __name__ == "__main__":
    main()
