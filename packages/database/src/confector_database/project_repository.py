from confector_core import Project, ProjectStatus
from sqlmodel import Session, select

from .models import ProjectTable


class SqliteProjectRepository:
    """Implementa confector_core.ProjectRepository. Nunca contiene lógica de negocio (11_DEVELOPMENT_GUIDELINES §15)."""

    def __init__(self, engine):
        self._engine = engine

    def add(self, project: Project) -> None:
        row = ProjectTable(
            id=project.id,
            name=project.name,
            client=project.client,
            status=project.status.value,
            created_at=project.created_at,
        )
        with Session(self._engine) as session:
            session.add(row)
            session.commit()

    def get(self, project_id: str) -> Project | None:
        with Session(self._engine) as session:
            row = session.get(ProjectTable, project_id)
            return self._to_domain(row) if row else None

    def list_all(self) -> list[Project]:
        with Session(self._engine) as session:
            rows = session.exec(select(ProjectTable)).all()
            return [self._to_domain(row) for row in rows]

    @staticmethod
    def _to_domain(row: ProjectTable) -> Project:
        return Project(
            id=row.id,
            name=row.name,
            client=row.client,
            status=ProjectStatus(row.status),
            created_at=row.created_at,
        )
