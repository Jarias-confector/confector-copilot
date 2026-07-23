from typing import Protocol

from .project import Project


class ProjectRepository(Protocol):
    """Puerto del dominio. La implementación (SQLite, etc.) vive en packages/database — 11_DEVELOPMENT_GUIDELINES §15."""

    def add(self, project: Project) -> None: ...

    def get(self, project_id: str) -> Project | None: ...

    def list_all(self) -> list[Project]: ...
