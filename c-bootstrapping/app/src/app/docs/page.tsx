export default function DocsPage() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-16">
      <h1 className="text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50">
        Documentation
      </h1>
      <p className="mt-4 text-zinc-600 dark:text-zinc-400">
        VM-Series bootstrap documentation will be rendered here. Topics include
        licensing, bootstrap packages, configuration files, and
        cloud-specific deployment workflows.
      </p>

      <div className="mt-8 rounded-lg border border-dashed border-zinc-300 bg-zinc-50 p-8 text-center text-sm text-zinc-500 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-400">
        Documentation content will be loaded from the docs/ directory.
      </div>
    </div>
  );
}
