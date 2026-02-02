"""Tests for ORM helper functions."""

import uuid
from datetime import datetime, timezone

from apps.shared_models.orm_helpers import job_from_api_response, job_from_create
from apps.shared_models.pydantic_api_models import Job, JobCreate


def test_job_from_create_maps_fields() -> None:
    payload = JobCreate(
        name="example",
        description="desc",
        url="https://example.com",
        retry_count=1,
        retry_delay=10,
        retry_limit=3,
        idempotency_key="abc123",
    )

    job = job_from_create(payload)

    assert job.name == "example"
    assert job.description == "desc"
    assert job.url == "https://example.com"
    assert job.retry_count == 1
    assert job.retry_delay == 10
    assert job.retry_limit == 3
    assert job.idempotency_key == "abc123"


def test_job_from_api_response_maps_fields() -> None:
    job_id = uuid.uuid4()
    timestamp = datetime.now(timezone.utc)
    payload = Job(
        id=job_id,
        name="example",
        description=None,
        url=None,
        status="pending",
        created_at=timestamp,
        updated_at=timestamp,
        retry_count=0,
        retry_delay=0,
        retry_limit=0,
        idempotency_key=None,
    )

    job = job_from_api_response(payload)

    assert job.id == job_id
    assert job.status == "pending"
    assert job.created_at == timestamp
    assert job.updated_at == timestamp
