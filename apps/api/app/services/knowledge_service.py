from confector_construction import extract
from confector_events import EventBus, event_types
from confector_knowledge_os import (
    Entity,
    EntityRepository,
    Relationship,
    RelationshipRepository,
    TimelineEvent,
    TimelineRepository,
    search_entities,
)


class KnowledgeService:
    """Application layer: Sprint 4 (Knowledge Engine MVP, 10_MVP_ROADMAP). Escucha DocumentProcessed."""

    def __init__(
        self,
        entity_repository: EntityRepository,
        relationship_repository: RelationshipRepository,
        timeline_repository: TimelineRepository,
        event_bus: EventBus,
    ):
        self._entities = entity_repository
        self._relationships = relationship_repository
        self._timeline = timeline_repository
        self._event_bus = event_bus

    def process_document(self, project_id: str, document_id: str, filename: str, extracted_text: str | None) -> None:
        if not extracted_text:
            self._timeline.add(
                TimelineEvent(
                    project_id=project_id,
                    description=f"Documento procesado sin texto extraíble: {filename}",
                    source_document_id=document_id,
                )
            )
            return

        entities, relationships = extract(extracted_text, project_id, document_id)
        for entity in entities:
            self._entities.add(entity)
        for relationship in relationships:
            self._relationships.add(relationship)

        if entities:
            self._event_bus.publish(
                event_types.ENTITY_DETECTED,
                {"count": len(entities), "document_id": document_id},
                project_id=project_id,
            )
        if relationships:
            self._event_bus.publish(
                event_types.RELATIONSHIP_DETECTED,
                {"count": len(relationships), "document_id": document_id},
                project_id=project_id,
            )

        description = (
            f"Se detectaron {len(entities)} entidades y {len(relationships)} relaciones en {filename}"
            if entities
            else f"Documento procesado sin entidades detectadas: {filename}"
        )
        self._timeline.add(TimelineEvent(project_id=project_id, description=description, source_document_id=document_id))

        self._event_bus.publish(event_types.KNOWLEDGE_UPDATED, {"document_id": document_id}, project_id=project_id)
        self._event_bus.publish(event_types.TIMELINE_UPDATED, {"document_id": document_id}, project_id=project_id)

    def list_entities(self, project_id: str) -> list[Entity]:
        return self._entities.list_by_project(project_id)

    def list_relationships(self, project_id: str) -> list[Relationship]:
        return self._relationships.list_by_project(project_id)

    def list_timeline(self, project_id: str) -> list[TimelineEvent]:
        return self._timeline.list_by_project(project_id)

    def search(self, project_id: str, query: str) -> list[Entity]:
        return search_entities(query, self._entities.list_by_project(project_id))
