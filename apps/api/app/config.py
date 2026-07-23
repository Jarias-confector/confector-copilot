from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("../../.env", ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    api_host: str = "127.0.0.1"
    api_port: int = 8000
    database_url: str = "sqlite:///./storage/confector.db"
    storage_dir: Path = Path("./storage")

    @property
    def exports_dir(self) -> Path:
        return self.storage_dir / "exports"

    @property
    def projects_dir(self) -> Path:
        return self.storage_dir / "projects"


settings = Settings()
