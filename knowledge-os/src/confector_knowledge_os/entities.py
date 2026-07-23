from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Protocol
from uuid import uuid4


@dataclass
class Entity:
    """Nodo genérico del Knowledge Graph. knowledge-os nunca sabe qué significa `type`
    (eso lo define el domain-pack, ADR-003) — solo lo persiste y lo relaciona."""

    project_id: str
    type: str
    label: str
    id: str = field(default_factory=lambda: str(uuid4()))
    properties: dict = field(default_factory=dict)
    source_document_id: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass
class Relationship:
    """Arista genérica entre dos entidades (04_KNOWLEDGE_MODEL §Relaciones)."""

    project_id: str
    from_entity_id: str
    type: str
    to_entity_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass
class TimelineEvent:
    """Evento inmutable de la cronología del proyecto (06_DOMAIN_MODEL §Cronología: nunca se edita, solo se agrega)."""

    project_id: str
    description: str
    id: str = field(default_factory=lambda: str(uuid4()))
    source_document_id: str | None = None
    occurred_at: datetime = field(default_factory=lambda: datetime.now(UTC))


class EntityRepository(Protocol):
    def add(self, entity: Entity) -> None: ...
    def list_by_project(self, project_id: str) -> list[Entity]: ...


class RelationshipRepository(Protocol):
    def add(self, relationship: Relationship) -> None: ...
    def list_by_project(self, project_id: str) -> list[Relationship]: ...


class TimelineRepository(Protocol):
    def add(self, event: TimelineEvent) -> None: ...
    def list_by_project(self, project_id: str) -> list[TimelineEvent]: ...
