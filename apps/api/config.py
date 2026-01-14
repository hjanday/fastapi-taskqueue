"""Configuration management for the FastAPI application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True

    # Application Settings
    app_name: str = "fastapi-taskqueue"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True
    
    # Database
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/taskqueue"

    # Logging
    log_level: str = "INFO"


settings = Settings()
