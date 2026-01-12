# FastAPI Task Queue - Documentation

## Overview

This is a task queue system built with FastAPI, AWS services, and Kubernetes. The system provides a control plane API for managing tasks and a worker system for processing them.

## Architecture

### Components

1. **Control Plane API** (`apps/api/`)
   - FastAPI-based REST API
   - Handles task submission, querying, and management
   - Provides health checks and monitoring endpoints

2. **Worker** (`apps/worker/`)
   - Task processing system (to be implemented)
   - Consumes tasks from queue
   - Reports task status back to control plane

3. **Infrastructure** (`infra/`)
   - Kubernetes manifests for deployment
   - Optional Terraform configurations for AWS resources

### System Design

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Client    │─────▶│  API Server │─────▶│    Queue    │
└─────────────┘      └─────────────┘      └─────────────┘
                                                   │
                                                   ▼
                                           ┌─────────────┐
                                           │   Worker    │
                                           └─────────────┘
```

### Technology Stack

- **API Framework**: FastAPI
- **Language**: Python 3.11+
- **Type Checking**: mypy
- **Linting/Formatting**: ruff
- **Testing**: pytest
- **Container Orchestration**: Kubernetes
- **Cloud Provider**: AWS (planned)

## Project Structure

```
.
├── apps/
│   ├── api/           # FastAPI control plane
│   │   ├── main.py    # Application entry point
│   │   ├── config.py  # Configuration management
│   │   └── __init__.py
│   └── worker/        # Task worker (future)
├── infra/
│   └── k8s/           # Kubernetes manifests
├── docs/              # Documentation
├── tests/             # Test suite
├── pyproject.toml     # Project configuration
├── Makefile           # Common commands
└── .env.example       # Environment variables template
```

## Getting Started

See [API.md](API.md) for API documentation and usage examples.

## Development

### Prerequisites

- Python 3.11+
- uv (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/hjanday/fastapi-taskqueue.git
   cd fastapi-taskqueue
   ```

2. Install dependencies:
   ```bash
   make dev
   ```

3. Copy the environment example:
   ```bash
   cp .env.example .env
   ```

4. Run the development server:
   ```bash
   make run
   ```

### Development Commands

- `make lint` - Run linter
- `make format` - Format code
- `make typecheck` - Run type checker
- `make test` - Run tests
- `make test-cov` - Run tests with coverage

## Deployment

Deployment configurations are available in the `infra/` directory (to be implemented).

## Contributing

1. Follow the existing code style
2. Ensure all tests pass
3. Add tests for new features
4. Update documentation as needed
