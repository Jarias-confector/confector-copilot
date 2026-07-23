import { useEffect, useState } from "react";
import { api, type DocumentItem, type Project, type Summary } from "./api";

function ProjectCard({ project }: { project: Project }) {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [documents, setDocuments] = useState<DocumentItem[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [uploading, setUploading] = useState(false);

  const loadDocuments = () => {
    api
      .listDocuments(project.id)
      .then(setDocuments)
      .catch(() => setError("No se pudieron cargar los documentos."));
  };

  useEffect(loadDocuments, [project.id]);

  const handleSummary = async () => {
    try {
      setSummary(await api.generateSummary(project.id));
    } catch {
      setError("No se pudo generar el resumen.");
    }
  };

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (!file) return;
    setUploading(true);
    try {
      await api.uploadDocument(project.id, file);
      loadDocuments();
    } catch {
      setError("No se pudo subir el documento.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <li className="rounded-lg border border-slate-200 bg-white p-4">
      <div className="flex items-center justify-between">
        <div>
          <p className="font-medium">{project.name}</p>
          <p className="text-sm text-slate-500">{project.client ?? "Sin cliente"}</p>
        </div>
        <div className="flex items-center gap-2">
          <label className="cursor-pointer rounded-md border border-slate-300 px-3 py-1.5 text-sm hover:bg-slate-50">
            {uploading ? "Subiendo…" : "Subir documento"}
            <input type="file" className="hidden" onChange={handleUpload} disabled={uploading} />
          </label>
          <button
            onClick={handleSummary}
            className="rounded-md border border-slate-300 px-3 py-1.5 text-sm hover:bg-slate-50"
          >
            Generar resumen
          </button>
        </div>
      </div>

      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}

      {documents.length > 0 && (
        <ul className="mt-3 flex flex-col gap-1.5">
          {documents.map((doc) => (
            <li key={doc.id} className="flex items-center gap-2 text-sm text-slate-600">
              <span className="rounded bg-slate-100 px-1.5 py-0.5 text-xs font-medium uppercase text-slate-500">
                {doc.kind}
              </span>
              <span>{doc.filename}</span>
              {Object.entries(doc.metadata).map(([key, value]) => (
                <span key={key} className="text-xs text-slate-400">
                  {key}: {value}
                </span>
              ))}
              <span className="text-xs text-slate-400">
                {doc.extracted_text ? "procesado" : "sin extracción"}
              </span>
            </li>
          ))}
        </ul>
      )}

      {summary && (
        <pre className="mt-3 whitespace-pre-wrap rounded-md bg-slate-50 p-3 text-xs text-slate-700">
          {summary.content}
        </pre>
      )}
    </li>
  );
}

export default function App() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [name, setName] = useState("");
  const [client, setClient] = useState("");
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

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b border-slate-200 bg-white px-8 py-5">
        <h1 className="text-xl font-semibold">CONFECTOR Copilot</h1>
        <p className="text-sm text-slate-500">Sprint 0 + Sprint 2 — Document Intelligence</p>
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
            <ProjectCard key={project.id} project={project} />
          ))}
          {projects.length === 0 && !error && (
            <li className="text-sm text-slate-500">Comienza creando un proyecto.</li>
          )}
        </ul>
      </main>
    </div>
  );
}
