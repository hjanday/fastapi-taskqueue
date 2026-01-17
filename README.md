# fastapi-taskqueue

A toy project designed to learn FastAPI, task queue basics, Docker, and Kubernetes.

## Overview

This project is to learn exploring distributed system concepts and cloud-native architecture. I build a task queue system to demonstrate:
- **FastAPI** - Building robust REST APIs
- **Task Queues** - Understanding asynchronous background processing
- **Docker & Kubernetes** - Containerization and orchestration mechanics

## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package installer

### Installation

1. Clone the repository:
```bash
git clone https://github.com/hjanday/fastapi-taskqueue.git
cd fastapi-taskqueue
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
make dev
```

3. Copy the environment example:
```bash
cp .env.example .env
```

### Running the API

Start the development server:
```bash
make run
```

The API will be available at http://localhost:8000

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Development Commands

```bash
make help       # Show all available commands
make lint       # Run code linter
make format     # Format code
make typecheck  # Run type checker
make test       # Run tests
make test-cov   # Run tests with coverage report
make clean      # Clean up cache files
```

## Project Structure

```
.
├── apps/
│   ├── api/           # FastAPI control plane
│   └── worker/        # Task worker (coming soon)
├── infra/
│   └── k8s/           # Kubernetes manifests (coming soon)
├── docs/              # Documentation
├── tests/             # Test suite
├── pyproject.toml     # Project configuration
├── Makefile           # Common development commands
└── .env.example       # Environment variables template
```

## Documentation

- [API Documentation](docs/API.md)
- [Architecture & Design](docs/README.md)

## Testing

Run the test suite:
```bash
make test
```

Run with coverage:
```bash
make test-cov
```

