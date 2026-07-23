from datetime import datetime
from sqlmodel import Field, SQLModel


class ProjectTable(SQLModel, table=True):
    __tablename__ = "projects"

    id: str = Field(primary_key=True)
    name: str
    client: str | None = None
    status: str = "active"
    created_at: datetime
