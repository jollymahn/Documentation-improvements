/* ══════════════════════════════════════════════════════════════════
   PAN Implementation Guides — Shared JavaScript
   Copy buttons, scroll spy, back-to-top, mobile sidebar, copy-as-markdown

   Usage: <script src="../../shared/js/pan-guides.js"></script>
   ══════════════════════════════════════════════════════════════════ */

// Copy-to-clipboard for code blocks
function copyCode(btn) {
  const code = btn.previousElementSibling.querySelector('code') || btn.previousElementSibling;
  navigator.clipboard.writeText(code.textContent).then(() => {
    btn.textContent = 'Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = 'Copy';
      btn.classList.remove('copied');
    }, 2000);
  });
}

// Scroll spy for sidebar active section
const sections = document.querySelectorAll('h2[id]');
const sidebarLinks = document.querySelectorAll('.sidebar a[data-section]');

function updateActiveSection() {
  let current = '';
  sections.forEach(section => {
    if (section.getBoundingClientRect().top <= 120) {
      current = section.id;
    }
  });
  sidebarLinks.forEach(link => {
    link.classList.toggle('active', link.dataset.section === current);
  });
}

// Back-to-top button
const backToTop = document.getElementById('backToTop');
function updateBackToTop() {
  if (backToTop) {
    backToTop.classList.toggle('visible', window.scrollY > 400);
  }
}

// Also show/hide the copy-as-markdown button with back-to-top
const copyMdBtn = document.getElementById('copyMdBtn');
function updateCopyMdBtn() {
  if (copyMdBtn) {
    copyMdBtn.classList.toggle('visible', window.scrollY > 400);
  }
}

// Close mobile sidebar on link click
sidebarLinks.forEach(link => {
  link.addEventListener('click', () => {
    const sidebar = document.querySelector('.sidebar');
    if (sidebar) sidebar.classList.remove('open');
  });
});

// Collapsible sections
document.querySelectorAll('.collapsible-header').forEach(header => {
  header.addEventListener('click', () => {
    header.classList.toggle('open');
    const body = header.nextElementSibling;
    if (body) body.classList.toggle('open');
  });
});

// Combined scroll handler
window.addEventListener('scroll', () => {
  updateActiveSection();
  updateBackToTop();
  updateCopyMdBtn();
}, { passive: true });

// Initial state
updateActiveSection();

/* ── Copy as Markdown ────────────────────────────────────────────── */

function htmlToMarkdown(el) {
  let md = '';

  function walk(node, listDepth) {
    if (node.nodeType === Node.TEXT_NODE) {
      return node.textContent;
    }
    if (node.nodeType !== Node.ELEMENT_NODE) return '';

    const tag = node.tagName.toLowerCase();

    // Skip non-content elements
    if (['script', 'style', 'button', 'nav', 'aside', 'header', 'footer'].includes(tag)) return '';
    if (node.classList.contains('breadcrumb') || node.classList.contains('cloud-links') ||
        node.classList.contains('copy-btn') || node.classList.contains('copy-md-btn') ||
        node.classList.contains('back-to-top') || node.classList.contains('sidebar') ||
        node.classList.contains('site-header')) return '';

    // Get children content
    let children = '';
    node.childNodes.forEach(child => { children += walk(child, listDepth); });
    children = children.replace(/\n{3,}/g, '\n\n');

    switch (tag) {
      case 'h1': return '\n# ' + children.trim() + '\n\n';
      case 'h2': return '\n## ' + children.trim() + '\n\n';
      case 'h3': return '\n### ' + children.trim() + '\n\n';
      case 'h4': return '\n#### ' + children.trim() + '\n\n';
      case 'p': return children.trim() + '\n\n';
      case 'br': return '\n';
      case 'hr': return '\n---\n\n';
      case 'strong': case 'b': return '**' + children.trim() + '**';
      case 'em': case 'i': return '*' + children.trim() + '*';
      case 'code':
        if (node.parentElement && node.parentElement.tagName === 'PRE') return children;
        return '`' + children.trim() + '`';
      case 'pre': {
        const code = node.querySelector('code');
        const text = code ? code.textContent : node.textContent;
        return '\n```\n' + text.trim() + '\n```\n\n';
      }
      case 'a': {
        const href = node.getAttribute('href');
        if (!href || href.startsWith('#')) return children;
        return '[' + children.trim() + '](' + href + ')';
      }
      case 'img': {
        const alt = node.getAttribute('alt') || '';
        const src = node.getAttribute('src') || '';
        return '![' + alt + '](' + src + ')\n\n';
      }
      case 'ul': {
        let items = '';
        node.querySelectorAll(':scope > li').forEach(li => {
          const indent = '  '.repeat(listDepth);
          const content = walk(li, listDepth + 1).trim().replace(/\n/g, '\n' + indent + '  ');
          items += indent + '- ' + content + '\n';
        });
        return '\n' + items + '\n';
      }
      case 'ol': {
        let items = '';
        let i = 1;
        node.querySelectorAll(':scope > li').forEach(li => {
          const indent = '  '.repeat(listDepth);
          const content = walk(li, listDepth + 1).trim().replace(/\n/g, '\n' + indent + '   ');
          items += indent + (i++) + '. ' + content + '\n';
        });
        return '\n' + items + '\n';
      }
      case 'li': return children;
      case 'table': {
        const rows = [];
        node.querySelectorAll('tr').forEach(tr => {
          const cells = [];
          tr.querySelectorAll('th, td').forEach(cell => {
            cells.push(walk(cell, 0).trim().replace(/\n/g, ' '));
          });
          rows.push(cells);
        });
        if (rows.length === 0) return '';
        const colCount = Math.max(...rows.map(r => r.length));
        let table = '';
        rows.forEach((row, idx) => {
          table += '| ' + row.join(' | ') + ' |\n';
          if (idx === 0) {
            table += '|' + ' --- |'.repeat(colCount) + '\n';
          }
        });
        return '\n' + table + '\n';
      }
      case 'th': case 'td': case 'tr': case 'thead': case 'tbody':
        return children;
      case 'div': {
        // Handle callout boxes
        if (node.classList.contains('callout')) {
          const title = node.querySelector('.callout-title');
          const titleText = title ? title.textContent.trim() : 'Note';
          const bodyContent = [];
          node.childNodes.forEach(child => {
            if (child !== title) bodyContent.push(walk(child, listDepth));
          });
          return '\n> **' + titleText + ':** ' + bodyContent.join('').trim().replace(/\n/g, '\n> ') + '\n\n';
        }
        // Handle code blocks wrapped in div.code-block
        if (node.classList.contains('code-block')) {
          const pre = node.querySelector('pre');
          if (pre) return walk(pre, listDepth);
        }
        return children;
      }
      default: return children;
    }
  }

  md = walk(el, 0);
  // Clean up excessive newlines
  md = md.replace(/\n{3,}/g, '\n\n').trim();
  return md;
}

function copyAsMarkdown() {
  const article = document.querySelector('.article');
  if (!article) return;

  const md = htmlToMarkdown(article);
  const btn = document.getElementById('copyMdBtn');

  navigator.clipboard.writeText(md).then(() => {
    const original = btn.innerHTML;
    btn.innerHTML = '<span style="font-size:1rem">&#10003;</span> Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.innerHTML = original;
      btn.classList.remove('copied');
    }, 2500);
  });
}
