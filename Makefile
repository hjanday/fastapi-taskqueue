.PHONY: help install dev lint format typecheck test test-cov clean run

help:  ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	uv pip install -e .

dev:  ## Install development dependencies
	uv pip install -e ".[dev]"

lint:  ## Run ruff linter
	ruff check .

format:  ## Format code with ruff
	ruff format .
	ruff check --fix .

typecheck:  ## Run mypy type checker
	mypy apps/

test:  ## Run tests
	pytest

test-cov:  ## Run tests with coverage report
	pytest --cov --cov-report=html --cov-report=term

clean:  ## Clean up cache and build files
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

run:  ## Run the API server
	uvicorn apps.api.main:app --host 0.0.0.0 --port 8000 --reload

run-prod:  ## Run the API server in production mode
	uvicorn apps.api.main:app --host 0.0.0.0 --port 8000
