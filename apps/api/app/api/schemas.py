from datetime import datetime

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    client: str | None = None


class ProjectOut(BaseModel):
    id: str
    name: str
    client: str | None
    status: str
    created_at: datetime


class SummaryOut(BaseModel):
    project_id: str
    file: str
    content: str


class DocumentOut(BaseModel):
    id: str
    project_id: str
    filename: str
    kind: str
    size_bytes: int
    extracted_text: str | None
    metadata: dict
    created_at: datetime
