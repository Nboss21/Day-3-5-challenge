from __future__ import annotations

from pathlib import Path
from typing import List

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from chimera.skills import TrendFetcher


class TrendReport(BaseModel):
    topic: str = Field(..., description="Title for the trend")
    source_urls: List[str] = Field(default_factory=list)
    summary: str
    credibility_score: float = Field(..., ge=0.0, le=1.0)
    velocity: str
    timestamp: str


app = FastAPI(title="Project Chimera API")


_frontend_path = Path(__file__).resolve().parent.parent / "frontend_placeholder"

# Actual frontend lives at project root /frontend; we resolve from CWD
ROOT_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = ROOT_DIR / "frontend"


if FRONTEND_DIR.exists():
    app.mount(
        "/static",
        StaticFiles(directory=str(FRONTEND_DIR), html=False),
        name="static",
    )


@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    """Serve the frontend index.html page."""
    index_path = FRONTEND_DIR / "index.html"
    if not index_path.exists():
        return "<h1>Project Chimera</h1><p>Frontend not found.</p>"
    return index_path.read_text(encoding="utf-8")


_fetcher = TrendFetcher()


@app.get("/api/trends", response_model=List[TrendReport])
async def get_trends(
    sources: List[str] = Query(default=["twitter"], description="Data sources to inspect"),
    lookback_hours: int = Query(default=24, ge=1, le=168),
) -> List[TrendReport]:
    """Return a small list of mock TrendReports for now.

    This wraps the TrendFetcher skill to expose it over HTTP.
    """

    items: List[TrendReport] = []
    for _ in range(5):
        raw = _fetcher.execute({"sources": sources, "lookback_hours": lookback_hours})
        items.append(TrendReport(**raw))
    return items
