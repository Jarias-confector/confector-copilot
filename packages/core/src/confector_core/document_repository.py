from typing import Protocol

from .document import Document


class DocumentRepository(Protocol):
    """Puerto del dominio. Implementación en packages/database (11_DEVELOPMENT_GUIDELINES §15)."""

    def add(self, document: Document) -> None: ...

    def list_by_project(self, project_id: str) -> list[Document]: ...
