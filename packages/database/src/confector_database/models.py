from datetime import datetime
from sqlmodel import Field, SQLModel


class ProjectTable(SQLModel, table=True):
    __tablename__ = "projects"

    id: str = Field(primary_key=True)
    name: str
    client: str | None = None
    status: str = "active"
    created_at: datetime


class DocumentTable(SQLModel, table=True):
    __tablename__ = "documents"

    id: str = Field(primary_key=True)
    project_id: str = Field(index=True)
    filename: str
    kind: str
    size_bytes: int
    storage_path: str
    extracted_text: str | None = None
    metadata_json: str = "{}"
    created_at: datetime


class EntityTable(SQLModel, table=True):
    __tablename__ = "entities"

    id: str = Field(primary_key=True)
    project_id: str = Field(index=True)
    type: str
    label: str
    properties_json: str = "{}"
    source_document_id: str | None = None
    created_at: datetime


class RelationshipTable(SQLModel, table=True):
    __tablename__ = "relationships"

    id: str = Field(primary_key=True)
    project_id: str = Field(index=True)
    from_entity_id: str
    type: str
    to_entity_id: str
    created_at: datetime


class TimelineEventTable(SQLModel, table=True):
    __tablename__ = "timeline_events"

    id: str = Field(primary_key=True)
    project_id: str = Field(index=True)
    description: str
    source_document_id: str | None = None
    occurred_at: datetime
