from pathlib import Path

from confector_ai_models import LLMProvider
from confector_core import Project, ProjectRepository
from confector_events import EventBus, event_types
from confector_exporters import generate_project_summary


class ProjectService:
    """Application layer: casos de uso. Coordina dominio (core) + infraestructura (database, ai_models, exporters)."""

    def __init__(
        self,
        repository: ProjectRepository,
        llm_provider: LLMProvider,
        exports_dir: Path,
        event_bus: EventBus,
    ):
        self._repository = repository
        self._llm_provider = llm_provider
        self._exports_dir = exports_dir
        self._event_bus = event_bus

    def create_project(self, name: str, client: str | None) -> Project:
        project = Project(name=name, client=client)
        self._repository.add(project)
        self._event_bus.publish(event_types.PROJECT_CREATED, {"name": name}, project_id=project.id)
        return project

    def list_projects(self) -> list[Project]:
        return self._repository.list_all()

    def generate_summary(self, project_id: str) -> Path:
        project = self._repository.get(project_id)
        if project is None:
            raise ValueError(f"Proyecto no encontrado: {project_id}")
        prompt = f"Genera un resumen ejecutivo breve para el proyecto '{project.name}' (cliente: {project.client or 'N/A'})."
        ai_output = self._llm_provider.generate(prompt)
        return generate_project_summary(project, ai_output, self._exports_dir)
