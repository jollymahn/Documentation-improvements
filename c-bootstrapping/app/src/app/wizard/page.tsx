export default function WizardPage() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-16">
      <h1 className="text-3xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50">
        Bootstrap Wizard
      </h1>
      <p className="mt-4 text-zinc-600 dark:text-zinc-400">
        The interactive wizard will guide you through generating a bootstrap
        package for your VM-Series deployment.
      </p>

      <div className="mt-8 rounded-lg border border-dashed border-zinc-300 bg-zinc-50 p-8 text-center text-sm text-zinc-500 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-400">
        Interactive wizard steps will appear here.
      </div>
    </div>
  );
}
