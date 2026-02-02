# Agent Instructions

## Product spec (MVP)

### Goal
Deliver a minimal task queue service with a control plane API and a worker that can
reliably execute jobs and report status.

### Required capabilities
- **Create jobs** with idempotency support, retries, and optional payload/URL.
- **Persist jobs** in the database with status transitions.
- **Dispatch jobs** to a queue/worker process.
- **Process jobs** in a worker, updating status and retry metadata.
- **Expose status** via API for job detail and list views.
- **Health/metrics** endpoints for API and worker readiness.

### Non-goals (for MVP)
- Multi-tenant auth, rate limiting, or advanced scheduling.
- Complex workflow DAGs.
- WebSocket updates.

## Repository layout
- `apps/api/`: FastAPI control plane and REST endpoints.
- `apps/worker/`: Background worker process (job execution loop).
- `apps/shared_models/`: Shared SQLAlchemy + Pydantic models, DB session utilities.
- `docs/`: Architecture and API documentation.
- `tests/`: Unit/integration tests.
- `infra/`: Infrastructure manifests (Kubernetes, etc.).

## Expectations for changes
- Keep API request/response shapes aligned with `apps/shared_models/pydantic_api_models.py`.
- Database schema changes should be reflected in `apps/shared_models/alchemy_models.py` and migrations.
- Update `docs/API.md` when endpoints change.
- Add tests and update `TESTS.md` when adding new functionality.
