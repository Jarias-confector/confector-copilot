import json

from confector_knowledge_os import Entity, Relationship, TimelineEvent
from sqlmodel import Session, select

from .models import EntityTable, RelationshipTable, TimelineEventTable


class SqliteEntityRepository:
    def __init__(self, engine):
        self._engine = engine

    def add(self, entity: Entity) -> None:
        row = EntityTable(
            id=entity.id,
            project_id=entity.project_id,
            type=entity.type,
            label=entity.label,
            properties_json=json.dumps(entity.properties),
            source_document_id=entity.source_document_id,
            created_at=entity.created_at,
        )
        with Session(self._engine) as session:
            session.add(row)
            session.commit()

    def list_by_project(self, project_id: str) -> list[Entity]:
        with Session(self._engine) as session:
            rows = session.exec(select(EntityTable).where(EntityTable.project_id == project_id)).all()
            return [
                Entity(
                    id=row.id,
                    project_id=row.project_id,
                    type=row.type,
                    label=row.label,
                    properties=json.loads(row.properties_json or "{}"),
                    source_document_id=row.source_document_id,
                    created_at=row.created_at,
                )
                for row in rows
            ]


class SqliteRelationshipRepository:
    def __init__(self, engine):
        self._engine = engine

    def add(self, relationship: Relationship) -> None:
        row = RelationshipTable(
            id=relationship.id,
            project_id=relationship.project_id,
            from_entity_id=relationship.from_entity_id,
            type=relationship.type,
            to_entity_id=relationship.to_entity_id,
            created_at=relationship.created_at,
        )
        with Session(self._engine) as session:
            session.add(row)
            session.commit()

    def list_by_project(self, project_id: str) -> list[Relationship]:
        with Session(self._engine) as session:
            rows = session.exec(select(RelationshipTable).where(RelationshipTable.project_id == project_id)).all()
            return [
                Relationship(
                    id=row.id,
                    project_id=row.project_id,
                    from_entity_id=row.from_entity_id,
                    type=row.type,
                    to_entity_id=row.to_entity_id,
                    created_at=row.created_at,
                )
                for row in rows
            ]


class SqliteTimelineRepository:
    def __init__(self, engine):
        self._engine = engine

    def add(self, event: TimelineEvent) -> None:
        row = TimelineEventTable(
            id=event.id,
            project_id=event.project_id,
            description=event.description,
            source_document_id=event.source_document_id,
            occurred_at=event.occurred_at,
        )
        with Session(self._engine) as session:
            session.add(row)
            session.commit()

    def list_by_project(self, project_id: str) -> list[TimelineEvent]:
        with Session(self._engine) as session:
            rows = session.exec(
                select(TimelineEventTable)
                .where(TimelineEventTable.project_id == project_id)
                .order_by(TimelineEventTable.occurred_at)
            ).all()
            return [
                TimelineEvent(
                    id=row.id,
                    project_id=row.project_id,
                    description=row.description,
                    source_document_id=row.source_document_id,
                    occurred_at=row.occurred_at,
                )
                for row in rows
            ]
