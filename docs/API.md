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

## Future Endpoints

The following endpoints are planned for future releases:

### Tasks

- `POST /tasks` - Create a new task
- `GET /tasks` - List all tasks
- `GET /tasks/{task_id}` - Get task details
- `DELETE /tasks/{task_id}` - Cancel a task
- `GET /tasks/{task_id}/status` - Get task status

### Queue Management

- `GET /queue/stats` - Get queue statistics
- `GET /queue/health` - Check queue health

## Versioning

The API version is included in the application metadata. Future versions may introduce versioned endpoints (e.g., `/v1/tasks`).

## Rate Limiting

Rate limiting is not yet implemented. This section will be updated as rate limiting is added.

## WebSocket Support

WebSocket support for real-time task updates is planned for future releases.
