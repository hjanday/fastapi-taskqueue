"""Job-related API endpoints."""

from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.shared_models.alchemy_models import Job
from apps.shared_models.database import get_db
from apps.shared_models.orm_helpers import job_from_create
from apps.shared_models.pydantic_api_models import JobCreate, Job as JobSchema

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("", response_model=JobSchema, status_code=status.HTTP_201_CREATED)
async def create_job(
    payload: JobCreate, db: AsyncSession = Depends(get_db)
) -> JobSchema:
    """Create a new job with optional idempotency handling."""
    if payload.idempotency_key:
        existing = await db.execute(
            select(Job).where(Job.idempotency_key == payload.idempotency_key)
        )
        job = existing.scalar_one_or_none()
        if job:
            return JobSchema.model_validate(job)

    job = job_from_create(payload)
    db.add(job)
    await db.commit()
    await db.refresh(job)
    return JobSchema.model_validate(job)


@router.get("", response_model=List[JobSchema])
async def list_jobs(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
) -> List[JobSchema]:
    """List jobs with basic pagination."""
    result = await db.execute(select(Job).offset(offset).limit(limit))
    jobs = result.scalars().all()
    return [JobSchema.model_validate(job) for job in jobs]


@router.get("/{job_id}", response_model=JobSchema)
async def get_job(job_id: UUID, db: AsyncSession = Depends(get_db)) -> JobSchema:
    """Fetch a single job by ID."""
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return JobSchema.model_validate(job)


@router.get("/{job_id}/status")
async def get_job_status(
    job_id: UUID, db: AsyncSession = Depends(get_db)
) -> dict:
    """Fetch job status by ID."""
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return {"id": job.id, "status": job.status}


@router.delete("/{job_id}", status_code=status.HTTP_202_ACCEPTED)
async def cancel_job(job_id: UUID, db: AsyncSession = Depends(get_db)) -> dict:
    """Cancel a job (scaffolded as a status update)."""
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    job.status = "failed"
    await db.commit()
    return {"id": job.id, "status": job.status, "message": "Job cancelled"}
