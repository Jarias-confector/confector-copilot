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


class EntityOut(BaseModel):
    id: str
    project_id: str
    type: str
    label: str
    properties: dict
    source_document_id: str | None
    created_at: datetime


class RelationshipOut(BaseModel):
    id: str
    project_id: str
    from_entity_id: str
    type: str
    to_entity_id: str
    created_at: datetime


class TimelineEventOut(BaseModel):
    id: str
    project_id: str
    description: str
    source_document_id: str | None
    occurred_at: datetime
