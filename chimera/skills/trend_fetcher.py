from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from chimera.core.skills import BaseSkill


class TrendFetcher(BaseSkill):
    """Simple stub implementation of a trend fetching skill.

    For now this returns mock data that matches the TrendReport
    contract in specs/technical.md so higher layers and the
    frontend can integrate against a stable schema.
    """

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        sources: List[str] = list(payload.get("sources", [])) or ["twitter"]

        return {
            "topic": "AI Agents and Autonomy",
            "source_urls": [
                "https://example.com/articles/ai-agents-overview",
            ],
            "summary": (
                "Daily snapshot of AI agent frameworks, governance "
                "patterns, and safety discussions across tech media."
            ),
            "credibility_score": 0.92,
            "velocity": "RISING",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "sources": sources,
        }
