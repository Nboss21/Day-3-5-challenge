# Project Chimera

Project Chimera is an agentic infrastructure "Factory" for building autonomous AI influencers.
The focus is on **Spec-Driven Development**, **governance**, and **safety nets** so that human
engineers and AI agents can collaborate safely.

## Key Directories

- `specs/` – Source of truth for intent
  - `_meta.md` – Vision and constraints
  - `functional.md` – User stories and agent roles
  - `technical.md` – API contracts and DB ERD
  - `openclaw_integration.md` – Strategy for the Agent Social Network
- `research/` – Architecture and tooling strategy notes
- `skills/` – Runtime skill contracts and design
- `tests/` – Failing tests that define the "empty slots" agents must fill
- `.cursor/rules` – IDE / AI agent behavior and prime directive

## Development Workflow

1. **Specs First**: Update `specs/` before writing implementation code.
2. **TDD**: Add or update tests in `tests/` based on the technical spec.
3. **Run Checks**:
   - `make setup` – Sync dependencies via `uv`
   - `make lint` – Run `ruff` style checks
   - `make security` – Run `bandit` security scan
   - `make spec-check` – Minimal spec compliance check
   - `make test` – Run the (intentionally failing) test suite
   - `make docker-test` – Build and run tests in Docker
   - `make serve` – Start the HTTP API and frontend at http://127.0.0.1:8000

## Frontend & API

- Backend API lives under the `chimera` package. A minimal
  `TrendFetcher` skill is exposed via `GET /api/trends` and
  returns mock `TrendReport` objects matching the Technical Spec.
- The browser frontend is in `frontend/` and is served by the
  FastAPI app as static files. It provides a simple “Scout
  dashboard” for fetching and visualising daily trends.

## CI/CD and Governance

GitHub Actions workflow in `.github/workflows/main.yml` runs linting, security checks,
spec-check, tests, and Docker-based tests on every push/PR to `main`.

AI review is configured via `.coderabbit.yaml` to emphasize spec alignment, schema
compliance, safety, and test coverage.
