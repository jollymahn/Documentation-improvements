export default function Home() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-16">
      <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50">
        VM-Series Bootstrap Guide
      </h1>
      <p className="mt-4 text-lg leading-8 text-zinc-600 dark:text-zinc-400">
        A comprehensive guide for bootstrapping Palo Alto Networks VM-Series
        firewalls across cloud environments. Configure licensing, initial
        setup, and Panorama connectivity before first boot.
      </p>

      <div className="mt-12 grid gap-6 sm:grid-cols-2">
        <a
          href="/docs"
          className="group rounded-lg border border-zinc-200 p-6 transition-colors hover:border-blue-300 hover:bg-blue-50/50 dark:border-zinc-800 dark:hover:border-blue-800 dark:hover:bg-blue-950/20"
        >
          <h2 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50">
            Documentation
          </h2>
          <p className="mt-2 text-sm text-zinc-600 dark:text-zinc-400">
            Browse the full bootstrap reference covering init-cfg.txt,
            bootstrap.xml, VM-auth keys, and cloud-specific workflows.
          </p>
        </a>

        <a
          href="/wizard"
          className="group rounded-lg border border-zinc-200 p-6 transition-colors hover:border-blue-300 hover:bg-blue-50/50 dark:border-zinc-800 dark:hover:border-blue-800 dark:hover:bg-blue-950/20"
        >
          <h2 className="text-xl font-semibold text-zinc-900 dark:text-zinc-50">
            Bootstrap Wizard
          </h2>
          <p className="mt-2 text-sm text-zinc-600 dark:text-zinc-400">
            Interactively generate bootstrap packages for AWS, Azure, or GCP
            with step-by-step guidance.
          </p>
        </a>
      </div>
    </div>
  );
}
