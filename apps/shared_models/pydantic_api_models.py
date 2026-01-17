"""
Pydantic schemas for the application.
"""
import uuid
from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, HttpUrl, ConfigDict


class JobBase(BaseModel):
    """Shared properties for Job models."""
    name: str
    description: Optional[str] = None
    url: Optional[str] = None  # Using str for simplicity, could be HttpUrl


class JobCreate(JobBase):
    """Properties to receive on item creation."""
    name: str
    description: Optional[str] = None
    url: Optional[str] = None
    retry_count: Optional[int] = None
    retry_delay: Optional[int] = None
    retry_limit: Optional[int] = None
    idempotency_key: Optional[str] = None


class Job(JobBase):
    """Properties to return to client."""
    id: uuid.UUID
    status: Literal["pending", "in_progress", "completed", "failed"]
    created_at: datetime
    updated_at: datetime
    retry_count: Optional[int] = None
    retry_delay: Optional[int] = None
    retry_limit: Optional[int] = None
    idempotency_key: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
