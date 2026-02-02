# API Documentation

## Overview

The FastAPI Task Queue API provides endpoints for managing and monitoring tasks in the queue system.

## Base URL

```
http://localhost:8000
```

## Endpoints

### Health Check

#### `GET /health`

Returns the health status of the API.

**Response:**
```json
{
  "status": "healthy"
}
```

**Status Codes:**
- `200 OK` - Service is healthy

---

### Root Endpoint

#### `GET /`

Returns basic information about the API.

**Response:**
```json
{
  "name": "fastapi-taskqueue",
  "version": "0.1.0",
  "status": "healthy"
}
```

**Status Codes:**
- `200 OK` - Success

---

### Metrics

#### `GET /metrics`

Returns a placeholder metrics payload.

**Response:**
```json
{
  "status": "ok",
  "metrics": {}
}
```

**Status Codes:**
- `200 OK` - Success

---

### Jobs

#### `POST /jobs`

Create a job with optional idempotency handling.

**Request Body:**
```json
{
  "name": "example",
  "description": "optional",
  "url": "https://example.com",
  "retry_count": 0,
  "retry_delay": 0,
  "retry_limit": 3,
  "idempotency_key": "optional-key"
}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "example",
  "description": "optional",
  "url": "https://example.com",
  "status": "pending",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z",
  "retry_count": 0,
  "retry_delay": 0,
  "retry_limit": 3,
  "idempotency_key": "optional-key"
}
```

**Status Codes:**
- `201 Created` - Job created
- `200 OK` - Existing job returned via idempotency key

---

#### `GET /jobs`

List jobs with pagination.

**Query Params:**
- `limit` (default 50)
- `offset` (default 0)

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "example",
    "description": "optional",
    "url": "https://example.com",
    "status": "pending",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "retry_count": 0,
    "retry_delay": 0,
    "retry_limit": 3,
    "idempotency_key": "optional-key"
  }
]
```

**Status Codes:**
- `200 OK` - Success

---

#### `GET /jobs/{job_id}`

Retrieve a single job by ID.

**Response:** Same as `POST /jobs` response.

**Status Codes:**
- `200 OK` - Success
- `404 Not Found` - Job does not exist

---

#### `GET /jobs/{job_id}/status`

Retrieve job status by ID.

**Response:**
```json
{
  "id": "uuid",
  "status": "pending"
}
```

**Status Codes:**
- `200 OK` - Success
- `404 Not Found` - Job does not exist

---

#### `DELETE /jobs/{job_id}`

Cancel a job (status update scaffold).

**Response:**
```json
{
  "id": "uuid",
  "status": "failed",
  "message": "Job cancelled"
}
```

**Status Codes:**
- `202 Accepted` - Cancellation recorded
- `404 Not Found` - Job does not exist

---

## Authentication

Authentication is not yet implemented. This section will be updated as authentication mechanisms are added.

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message description"
}
```

Common HTTP status codes:
- `400 Bad Request` - Invalid request parameters
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error
- `500 Internal Server Error` - Server error

## Interactive Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Examples

### Check API Health

```bash
curl -X GET http://localhost:8000/health
```

### Get API Information

```bash
curl -X GET http://localhost:8000/
```

### Create a Job

```bash
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"name": "example"}'
```

### List Jobs

```bash
curl -X GET "http://localhost:8000/jobs?limit=10&offset=0"
```

## Future Endpoints

The following endpoints are planned for future releases:

### Queue Management

- `GET /queue/stats` - Get queue statistics
- `GET /queue/health` - Check queue health

## Versioning

The API version is included in the application metadata. Future versions may introduce versioned endpoints (e.g., `/v1/jobs`).

## Rate Limiting

Rate limiting is not yet implemented. This section will be updated as rate limiting is added.

## WebSocket Support

WebSocket support for real-time task updates is planned for future releases.
