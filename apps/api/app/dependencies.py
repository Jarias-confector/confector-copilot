from functools import lru_cache

from confector_ai_models import get_default_provider
from confector_database import SqliteProjectRepository, get_engine

from app.config import settings
from app.services.project_service import ProjectService


@lru_cache
def get_project_service() -> ProjectService:
    engine = get_engine(settings.database_url)
    repository = SqliteProjectRepository(engine)
    llm_provider = get_default_provider()
    return ProjectService(repository, llm_provider, settings.exports_dir)
