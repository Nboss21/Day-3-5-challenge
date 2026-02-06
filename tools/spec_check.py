"""Minimal spec compliance check for Project Chimera.

This is intentionally lightweight: it verifies that the core spec files
exist and that the tests reference the primary contracts defined in
specs/technical.md (e.g., TrendReport and BaseSkill).

The goal is to give CI a concrete, automatable hook for "spec-check"
without over-engineering a full static analysis system.
"""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def assert_spec_files_exist() -> None:
    specs_dir = PROJECT_ROOT / "specs"
    required = ["_meta.md", "functional.md", "technical.md"]
    missing = [name for name in required if not (specs_dir / name).exists()]
    if missing:
        raise SystemExit(f"Missing required spec files in specs/: {missing}")


def assert_tests_reference_core_contracts() -> None:
    tests_dir = PROJECT_ROOT / "tests"
    if not tests_dir.exists():
        raise SystemExit("tests/ directory does not exist")

    content = "".join(p.read_text(encoding="utf-8") for p in tests_dir.glob("test_*.py"))

    required_markers = [
        "TrendFetcher",  # From tests/test_trend_fetcher.py
        "BaseSkill",  # From tests/test_skills_interface.py
        "credibility_score",  # From TrendReport contract
    ]

    missing_markers = [m for m in required_markers if m not in content]
    if missing_markers:
        raise SystemExit(
            "Tests do not appear to cover core spec contracts: " f"missing markers: {missing_markers}"
        )


def main() -> None:
    assert_spec_files_exist()
    assert_tests_reference_core_contracts()
    print("Spec check passed: core specs and test contracts are in place.")


if __name__ == "__main__":  # pragma: no cover
    main()
