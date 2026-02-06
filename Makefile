.PHONY: setup test lint security spec-check docker-test

setup:
	@echo "Setting up environment..."
	uv sync

test:
	@echo "Running tests..."
	uv run pytest tests/

lint:
	@echo "Running lint checks (ruff)..."
	uv run ruff check .

security:
	@echo "Running security checks (bandit)..."
	uv run bandit -q -r . || true

spec-check:
	@echo "Checking spec compliance..."
	uv run python -m tools.spec_check

docker-test:
	@echo "Building and running tests in Docker..."
	docker build -t project-chimera-ci .
	docker run --rm project-chimera-ci
