"""Helpers for translating API payloads into ORM models."""

from typing import Mapping, Union

from apps.shared_models.alchemy_models import Job
from apps.shared_models.pydantic_api_models import Job as JobSchema
from apps.shared_models.pydantic_api_models import JobCreate


JobPayload = Union[JobSchema, Mapping[str, object]]


def job_from_create(payload: JobCreate) -> Job:
    """Create a Job ORM instance from a JobCreate payload."""
    data = payload.model_dump(exclude_unset=True)
    return Job(**data)


def job_from_api_response(payload: JobPayload) -> Job:
    """Create a Job ORM instance from a Job API response payload."""
    if isinstance(payload, JobSchema):
        data = payload.model_dump()
    else:
        data = JobSchema.model_validate(payload).model_dump()
    return Job(**data)
