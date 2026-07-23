from pathlib import Path

from sqlmodel import SQLModel, create_engine

_engine = None


def get_engine(database_url: str):
    global _engine
    if _engine is None:
        if database_url.startswith("sqlite:///"):
            db_path = Path(database_url.removeprefix("sqlite:///"))
            db_path.parent.mkdir(parents=True, exist_ok=True)
        connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
        _engine = create_engine(database_url, connect_args=connect_args)
        SQLModel.metadata.create_all(_engine)
    return _engine
