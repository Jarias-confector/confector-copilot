from pathlib import Path

from confector_core import Document, DocumentRepository
from confector_events import EventBus, event_types

from app.workers.document_processor import classify, extract


class DocumentService:
    """Application layer: Sprint 2 (Document Intelligence, 10_MVP_ROADMAP)."""

    def __init__(self, repository: DocumentRepository, event_bus: EventBus, storage_dir: Path):
        self._repository = repository
        self._event_bus = event_bus
        self._storage_dir = storage_dir

    def upload_document(self, project_id: str, filename: str, content: bytes) -> Document:
        kind = classify(filename)
        document = Document(
            project_id=project_id,
            filename=filename,
            kind=kind,
            size_bytes=len(content),
            storage_path="",
        )

        project_dir = self._storage_dir / "projects" / project_id / "documents"
        project_dir.mkdir(parents=True, exist_ok=True)
        path = project_dir / f"{document.id}-{filename}"
        path.write_bytes(content)
        document.storage_path = str(path)

        self._event_bus.publish(
            event_types.DOCUMENT_UPLOADED,
            {"filename": filename, "kind": kind.value},
            project_id=project_id,
        )

        result = extract(kind, content, filename)
        document.extracted_text = result.text
        document.metadata = result.metadata
        self._repository.add(document)

        self._event_bus.publish(
            event_types.DOCUMENT_PROCESSED,
            {
                "document_id": document.id,
                "filename": filename,
                "kind": kind.value,
                "extracted": document.extracted_text is not None,
                "extracted_text": document.extracted_text,
            },
            project_id=project_id,
        )
        return document

    def list_documents(self, project_id: str) -> list[Document]:
        return self._repository.list_by_project(project_id)
