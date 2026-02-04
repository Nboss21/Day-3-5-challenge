# Project Chimera: The Agentic Infrastructure
**Meta-Specification & Vision Document**

## 1. Vision
To engineer a robust "Factory" for Autonomous AI Influencers that replaces fragile prompt-based "vibe coding" with a Spec-Driven, verifiable, and observable engineering environment. The goal is not just to build a bot, but to build the **infrastructure** that allows a swarm of agents to operate safely and effectively.

## 2. Core Philosophies
- **Spec-Driven Development (SDD)**: Application code is downstream of Specification. "Intent" is defined in Markdown/Mermaid before Python.
- **Traceability**: All agent actions are observable via the Tenx MCP Sense "Black Box".
- **Safety First**: No uncontrolled LLM loops. Every "social" action requires a Governor check and potential Human-in-the-Loop (HITL) approval.
- **Git Hygiene**: Atomic commits that tell a story of evolving complexity.

## 3. System Constraints
- **Runtime**: Python 3.12+ (managed via `uv`).
- **Database**: PostgreSQL for structured data; JSONB for flex-schema metadata.
- **Agent Framework**: OpenClaw (Inter-agent communication) + Custom Governance Layer.
- **Testing**: TDD is mandatory. Failing tests must exist *before* implementation.
- **Containerization**: Docker-first deployment. "It works on my machine" is invalid.

## 4. Definitions
- **The Factory**: The codebase and CI/CD pipeline.
- **The Governor**: The primary orchestrator agent that manages sub-agents (Scout, Writer, Artist).
- **The Skill**: A discrete, reusable capability (e.g., `download_video`, `transcribe_audio`) with a strict schema.
- **MCP Server**: An external bridge (filesystem, git, db) that providing grounding to the agent.

## 5. Success Metrics
- **Reliability**: Zero hallucinations in critical control paths (e.g., publishing).
- **Observability**: 100% of agent steps logged to MCP Sense.
- **Autonomy**: The swarm can generate a Release Candidate video with < 1 human intervention per week (target).
