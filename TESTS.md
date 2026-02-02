# Testing Plan

This document defines the testing strategy for the FastAPI task queue MVP.

## Test levels

### 1) Unit tests
**Goal:** Verify core logic without external dependencies.

- **Model validation**
  - Pydantic `JobCreate` validation (required fields, optional fields, idempotency key).
  - Status enum validation.
- **Database models**
  - SQLAlchemy `Job` defaults (status, retry fields).
- **Utility behavior**
  - Retry calculation logic (if introduced).
  - Idempotency key conflict handling (if implemented in API layer).

### 2) Integration tests
**Goal:** Validate API + DB behavior using a real or containerized database.

- **Job lifecycle**
  - `POST /tasks` creates a job and persists it.
  - `GET /tasks/{id}` returns correct job data.
  - `GET /tasks` returns pagination and filters (if added).
  - `DELETE /tasks/{id}` marks as cancelled (if supported).
- **Idempotency**
  - Repeated `POST /tasks` with same idempotency key returns existing job.
- **Status transitions**
  - `POST /tasks` sets `pending`.
  - Worker updates to `in_progress`, `completed`, `failed`.

### 3) Worker tests
**Goal:** Ensure worker consumes jobs and reports back.

- **Queue consumption**
  - Worker pulls a queued job and updates status.
- **Retry behavior**
  - Failure increments retry_count and respects retry_limit/delay.
- **Job execution**
  - URL-based job payload execution (if supported) with mocks.

### 4) Contract/API tests
**Goal:** Validate API schema and compatibility.

- OpenAPI schema snapshots for core endpoints.
- Response shape checks against `apps/shared_models/pydantic_api_models.py`.

### 5) End-to-end tests
**Goal:** Validate the full pipeline.

- Submit job -> queue -> worker -> completed status.
- Failure flow with retries -> failed status after retry limit.

## Test infrastructure

- **Database:** Use Postgres via docker-compose for integration/E2E tests.
- **Async testing:** Use `pytest-asyncio` or `anyio` with FastAPI TestClient.
- **Factories/fixtures:**
  - Job factory for model creation.
  - Database session fixture with rollback/cleanup per test.
- **Queue simulation:**
  - For MVP, allow in-memory queue adapter for fast tests.

## Coverage expectations

- Critical business logic: **>= 90%**.
- API handlers and models: **>= 80%**.

## CI checks (recommended)

- `make lint`
- `make format` (check only)
- `make typecheck`
- `make test`
- `make test-cov`
