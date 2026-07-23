const API_BASE = "http://127.0.0.1:8000";

export interface Project {
  id: string;
  name: string;
  client: string | null;
  status: string;
  created_at: string;
}

export interface Summary {
  project_id: string;
  file: string;
  content: string;
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!res.ok) {
    throw new Error(`${res.status} ${res.statusText}`);
  }
  return res.json();
}

export const api = {
  listProjects: () => request<Project[]>("/projects"),
  createProject: (name: string, client: string) =>
    request<Project>("/projects", {
      method: "POST",
      body: JSON.stringify({ name, client: client || null }),
    }),
  generateSummary: (projectId: string) =>
    request<Summary>(`/projects/${projectId}/summary`, { method: "POST" }),
};
