# Tooling & Skills Strategy

## 1. Developer Tools (MCP Architecture)
These tools empower the **Human Engineer** and the **IDE Agent** to build the system.

### 1.1 Core MCP Servers
- **Tenx MCP Sense**: The "Flight Recorder". Logs all agent actions for debugging and governance.
  - *Usage*: Connected at all times.
- **FileSystem MCP**: Standard file manipulation.
- **Git MCP**: Version control operations.
- **Postgres MCP** (Planned): Direct DB schema introspection.

### 1.2 Python Environment Tooling (uv)
- **Dependency Management**: `uv pip install ...`
- **Virtual Env**: Managed by `uv`.
- **Linting/Formatting**: `ruff` (Fast, typically replacing black/isort).

## 2. Agent Skills (Runtime)
These are capabilities available to the **Chimera Agents** at runtime.

### 2.1 Skill Architecture
- **Isolation**: Each skill is a standalone module or class.
- **Contract**: Must implement `BaseSkill` interface.
- **State**: Skills are stateless; context is passed in via `payload`.

### 2.2 Critical Skills List
1.  **`skill_trend_search`**:
    -   *Input*: `{ "query": str, "platforms": List[str] }`
    -   *Output*: `TrendReport` Object
2.  **`skill_generate_script`**:
    -   *Input*: `{ "topic": str, "style": str }`
    -   *Output*: `Script` Object
3.  **`skill_compile_video`**:
    -   *Input*: `{ "script": Script, "assets": List[Path] }`
    -   *Output*: Path to `.mp4`
