"""Tests for the API endpoints."""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """Test the root endpoint returns expected data."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "fastapi-taskqueue"
    assert data["version"] == "0.1.0"
    assert data["status"] == "healthy"


def test_health_endpoint(client: TestClient) -> None:
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
