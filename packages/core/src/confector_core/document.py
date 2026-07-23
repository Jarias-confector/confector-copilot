from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum
from uuid import uuid4


class DocumentKind(str, Enum):
    """Clasificación por tipo — 04_KNOWLEDGE_MODEL Nivel 1 (Información)."""

    PDF = "pdf"
    WORD = "word"
    EXCEL = "excel"
    CSV = "csv"
    PRESENTATION = "presentation"
    TEXT = "text"
    AUDIO = "audio"
    OTHER = "other"


@dataclass
class Document:
    """Representa cualquier archivo. Únicamente una fuente de información, no contiene lógica (06_DOMAIN_MODEL)."""

    project_id: str
    filename: str
    kind: DocumentKind
    size_bytes: int
    storage_path: str
    id: str = field(default_factory=lambda: str(uuid4()))
    extracted_text: str | None = None
    metadata: dict = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
