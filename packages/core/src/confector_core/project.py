from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum
from uuid import uuid4


class ProjectStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"


@dataclass
class Project:
    """Aggregate root. Representa una obra (06_DOMAIN_MODEL.md)."""

    name: str
    client: str | None = None
    id: str = field(default_factory=lambda: str(uuid4()))
    status: ProjectStatus = ProjectStatus.ACTIVE
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def archive(self) -> None:
        self.status = ProjectStatus.ARCHIVED

    def rename(self, name: str) -> None:
        if not name.strip():
            raise ValueError("El nombre del proyecto no puede estar vacío")
        self.name = name
