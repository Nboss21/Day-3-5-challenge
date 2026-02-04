# Functional Specification: The Swarm

## 1. Actors & Roles

### The Governor (System Admin / Orchestrator)
- **Role**: Manages the lifecycle of a Content Request.
- **Responsibilities**:
  - Receives high-level Intent from Human.
  - Delegates tasks to specialist agents.
  - Validates outputs against Specs (Schema Validation).
  - Handles the "Safety Gate" approval process.

### The Scout (Trend Researcher)
- **Role**: Identifying high-yield topics.
- **Responsibilities**:
  - Scrapes trusted sources (e.g., TechCrunch, Twitter/X, Reddit).
  - Filters noise using "Social Protocol" heuristics.
  - Outputs a structured `TrendReport`.

### The Writer (Scriptwriter)
- **Role**: Content generation.
- **Responsibilities**:
  - Consumes `TrendReport`.
  - Drafts scripts optimized for target platforms (Shorts vs Long-form).
  - Includes Citation links.

### The Artist (Media Producer)
- **Role**: Asset generation.
- **Responsibilities**:
  - Takes `Script` and generates/fetches visual assets.
  - Composes the final video utilizing FFMPEG or AI Video APIs.
  - Returns a `MediaAsset`.

## 2. User Stories

### Story 1: Trend Discovery
**As a** Governor,
**I want to** commission a daily trend report,
**So that** I know what topics are valid for content generation.
- **Acceptance Criteria**:
  - Scout returns top 5 trends.
  - Each trend has a `credibility_score` > 0.8.

### Story 2: Script Generation
**As a** Governor,
**I want to** transform a Trend into a Script,
**So that** the content is engaging and factually accurate.
- **Acceptance Criteria**:
  - Script length is within platform limits (e.g., < 60s for Shorts).
  - Tone matches the "Persona" config.

### Story 3: The Safety Gate (HITL)
**As a** Human Executive,
**I want to** approve the final video before it publishes,
**So that** no brand-damaging hallucinations go live.
- **Acceptance Criteria**:
  - System pauses at `state: AWAITING_APPROVAL`.
  - Notification sent to User.
  - Publish happens ONLY after `approve` signal.

### Story 4: Recursive Improvement (Self-Healing)
**As a** Governor,
**I want to** reject a Script that fails structure checks,
**So that** the Writer attempts a fix without human intervention.
- **Acceptance Criteria**:
  - If Script JSON is invalid, Governor sends error feedback back to Writer.
  - Writer retries up to 3 times.
