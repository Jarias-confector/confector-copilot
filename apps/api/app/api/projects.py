from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_project_service
from app.services.project_service import ProjectService

from .schemas import ProjectCreate, ProjectOut, SummaryOut

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectOut, status_code=201)
def create_project(payload: ProjectCreate, service: ProjectService = Depends(get_project_service)):
    project = service.create_project(payload.name, payload.client)
    return project


@router.get("", response_model=list[ProjectOut])
def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()


@router.post("/{project_id}/summary", response_model=SummaryOut)
def generate_summary(project_id: str, service: ProjectService = Depends(get_project_service)):
    try:
        path = service.generate_summary(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return SummaryOut(project_id=project_id, file=path.name, content=path.read_text(encoding="utf-8"))
