from confector_core import Document, DocumentKind
from sqlmodel import Session, select

from .models import DocumentTable


class SqliteDocumentRepository:
    """Implementa confector_core.DocumentRepository."""

    def __init__(self, engine):
        self._engine = engine

    def add(self, document: Document) -> None:
        row = DocumentTable(
            id=document.id,
            project_id=document.project_id,
            filename=document.filename,
            kind=document.kind.value,
            size_bytes=document.size_bytes,
            storage_path=document.storage_path,
            extracted_text=document.extracted_text,
            created_at=document.created_at,
        )
        with Session(self._engine) as session:
            session.add(row)
            session.commit()

    def list_by_project(self, project_id: str) -> list[Document]:
        with Session(self._engine) as session:
            rows = session.exec(
                select(DocumentTable).where(DocumentTable.project_id == project_id)
            ).all()
            return [self._to_domain(row) for row in rows]

    @staticmethod
    def _to_domain(row: DocumentTable) -> Document:
        return Document(
            id=row.id,
            project_id=row.project_id,
            filename=row.filename,
            kind=DocumentKind(row.kind),
            size_bytes=row.size_bytes,
            storage_path=row.storage_path,
            extracted_text=row.extracted_text,
            created_at=row.created_at,
        )
