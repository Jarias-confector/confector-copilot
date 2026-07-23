from fastapi import APIRouter, Depends

from app.dependencies import get_knowledge_service
from app.services.knowledge_service import KnowledgeService

from .schemas import EntityOut, RelationshipOut, TimelineEventOut

router = APIRouter(prefix="/projects/{project_id}", tags=["knowledge"])


@router.get("/entities", response_model=list[EntityOut])
def list_entities(project_id: str, service: KnowledgeService = Depends(get_knowledge_service)):
    return service.list_entities(project_id)


@router.get("/relationships", response_model=list[RelationshipOut])
def list_relationships(project_id: str, service: KnowledgeService = Depends(get_knowledge_service)):
    return service.list_relationships(project_id)


@router.get("/timeline", response_model=list[TimelineEventOut])
def list_timeline(project_id: str, service: KnowledgeService = Depends(get_knowledge_service)):
    return service.list_timeline(project_id)


@router.get("/search", response_model=list[EntityOut])
def search(project_id: str, q: str, service: KnowledgeService = Depends(get_knowledge_service)):
    return service.search(project_id, q)
