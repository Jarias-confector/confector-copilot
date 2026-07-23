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
    created_at: datetime
