
import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Enum, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .database import Base

# Job/Task Model
"""
Need: 
- Job ID
- Job Name
- Job Description
- Job Status
- Job Created At
- Job Updated At
- Job URL (S3)
- Job Retry Count
- Job Retry Delay
- Job Retry Limit
- Idempotency Key (this is to ensure no duplicate transactions get handled or two events get processed)
"""
class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        Enum("pending", "in_progress", "completed", "failed", name="job_status"),
        default="pending",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        onupdate=func.now()
    )
    url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    retry_count: Mapped[int] = mapped_column(Integer, default=0)
    retry_delay: Mapped[int] = mapped_column(Integer, default=0)
    retry_limit: Mapped[int] = mapped_column(Integer, default=0)
    idempotency_key: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
