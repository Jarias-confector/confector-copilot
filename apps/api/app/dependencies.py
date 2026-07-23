from functools import lru_cache

from confector_ai_models import get_default_provider
from confector_database import SqliteDocumentRepository, SqliteProjectRepository, get_engine

from app.config import settings
from app.events_setup import get_event_bus
from app.services.document_service import DocumentService
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
