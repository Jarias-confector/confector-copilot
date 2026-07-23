import { useEffect, useState } from "react";
import { api, type Project, type Summary } from "./api";

export default function App() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [name, setName] = useState("");
  const [client, setClient] = useState("");
  const [summaries, setSummaries] = useState<Record<string, Summary>>({});
  const [error, setError] = useState<string | null>(null);

  const loadProjects = () => {
    api
      .listProjects()
      .then(setProjects)
      .catch(() => setError("No se pudo conectar con el backend. ¿Está corriendo apps/api?"));
  };

  useEffect(loadProjects, []);

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;
    try {
      await api.createProject(name, client);
      setName("");
      setClient("");
      loadProjects();
    } catch {
      setError("No se pudo crear el proyecto.");
    }
  };

  const handleSummary = async (projectId: string) => {
    try {
      const summary = await api.generateSummary(projectId);
      setSummaries((prev) => ({ ...prev, [projectId]: summary }));
    } catch {
      setError("No se pudo generar el resumen.");
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b border-slate-200 bg-white px-8 py-5">
        <h1 className="text-xl font-semibold">CONFECTOR Copilot</h1>
        <p className="text-sm text-slate-500">Walking skeleton — Sprint 0</p>
      </header>

      <main className="mx-auto max-w-2xl px-8 py-10">
        {error && (
          <div className="mb-6 rounded-md border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {error}
          </div>
        )}

        <form onSubmit={handleCreate} className="mb-10 flex flex-wrap items-end gap-3">
          <div className="flex flex-col gap-1">
            <label className="text-sm font-medium text-slate-700">Proyecto</label>
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Casa Vida"
              className="rounded-md border border-slate-300 px-3 py-2 text-sm"
            />
          </div>
          <div className="flex flex-col gap-1">
            <label className="text-sm font-medium text-slate-700">Cliente</label>
            <input
              value={client}
              onChange={(e) => setClient(e.target.value)}
              placeholder="Familia Pérez"
              className="rounded-md border border-slate-300 px-3 py-2 text-sm"
            />
          </div>
          <button
            type="submit"
            className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-700"
          >
            Crear proyecto
          </button>
        </form>

        <ul className="flex flex-col gap-4">
          {projects.map((project) => (
            <li key={project.id} className="rounded-lg border border-slate-200 bg-white p-4">
              <div className="flex items-center justify-between">
                <div>
                  <p className="font-medium">{project.name}</p>
                  <p className="text-sm text-slate-500">{project.client ?? "Sin cliente"}</p>
                </div>
                <button
                  onClick={() => handleSummary(project.id)}
                  className="rounded-md border border-slate-300 px-3 py-1.5 text-sm hover:bg-slate-50"
                >
                  Generar resumen
                </button>
              </div>
              {summaries[project.id] && (
                <pre className="mt-3 whitespace-pre-wrap rounded-md bg-slate-50 p-3 text-xs text-slate-700">
                  {summaries[project.id].content}
                </pre>
              )}
            </li>
          ))}
          {projects.length === 0 && !error && (
            <li className="text-sm text-slate-500">Comienza creando un proyecto.</li>
          )}
        </ul>
      </main>
    </div>
  );
}
