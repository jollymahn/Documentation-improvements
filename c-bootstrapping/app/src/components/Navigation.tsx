"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navItems = [
  { href: "/", label: "Home" },
  { href: "/docs", label: "Documentation" },
  { href: "/wizard", label: "Bootstrap Wizard" },
];

export default function Navigation() {
  const pathname = usePathname();

  return (
    <header className="border-b border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-950">
      <nav className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
        <Link href="/" className="text-lg font-semibold tracking-tight">
          VM-Series Bootstrap
        </Link>
        <ul className="flex gap-6 text-sm font-medium">
          {navItems.map(({ href, label }) => (
            <li key={href}>
              <Link
                href={href}
                className={
                  pathname === href
                    ? "text-blue-600 dark:text-blue-400"
                    : "text-zinc-600 hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-zinc-100"
                }
              >
                {label}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
}
