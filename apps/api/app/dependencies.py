from functools import lru_cache

from confector_ai_models import get_default_provider
from confector_database import (
    SqliteDocumentRepository,
    SqliteEntityRepository,
    SqliteProjectRepository,
    SqliteRelationshipRepository,
    SqliteTimelineRepository,
    get_engine,
)
from confector_events import event_types

from app.config import settings
from app.events_setup import get_event_bus
from app.services.document_service import DocumentService
from app.services.knowledge_service import KnowledgeService
from app.services.project_service import ProjectService


@lru_cache
def get_project_service() -> ProjectService:
    engine = get_engine(settings.database_url)
    repository = SqliteProjectRepository(engine)
    llm_provider = get_default_provider()
    return ProjectService(repository, llm_provider, settings.exports_dir, get_event_bus())


@lru_cache
def get_document_service() -> DocumentService:
    engine = get_engine(settings.database_url)
    repository = SqliteDocumentRepository(engine)
    return DocumentService(repository, get_event_bus(), settings.storage_dir)


@lru_cache
def get_knowledge_service() -> KnowledgeService:
    engine = get_engine(settings.database_url)
    return KnowledgeService(
        SqliteEntityRepository(engine),
        SqliteRelationshipRepository(engine),
        SqliteTimelineRepository(engine),
        get_event_bus(),
    )


def wire_event_subscribers() -> None:
    """Knowledge Engine escucha DocumentProcessed (07_EVENT_ARCHITECTURE) — nunca se llama directamente."""

    def _on_document_processed(event) -> None:
        get_knowledge_service().process_document(
            project_id=event.project_id,
            document_id=event.payload["document_id"],
            filename=event.payload["filename"],
            extracted_text=event.payload.get("extracted_text"),
        )

    get_event_bus().subscribe(event_types.DOCUMENT_PROCESSED, _on_document_processed)
