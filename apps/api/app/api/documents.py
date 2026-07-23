from fastapi import APIRouter, Depends, File, UploadFile

from app.dependencies import get_document_service
from app.services.document_service import DocumentService

from .schemas import DocumentOut

router = APIRouter(prefix="/projects/{project_id}/documents", tags=["documents"])


@router.post("", response_model=DocumentOut, status_code=201)
async def upload_document(
    project_id: str,
    file: UploadFile = File(...),
    service: DocumentService = Depends(get_document_service),
):
    content = await file.read()
    document = service.upload_document(project_id, file.filename, content)
    return document


@router.get("", response_model=list[DocumentOut])
def list_documents(project_id: str, service: DocumentService = Depends(get_document_service)):
    return service.list_documents(project_id)
