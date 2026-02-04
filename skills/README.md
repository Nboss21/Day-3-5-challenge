# Chimera Skills Library

This directory contains the runtime capabilities (Skills) for the Agent Swarm.

## The Skill Interface
All skills inherit from `BaseSkill` and must validate inputs/outputs against Pydantic models.

```python
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseSkill(ABC):
    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Run the skill logic"""
        pass
```

## Available Skills

### 1. `skill_fetch_trends`
Scrapes external sources for trending topics.
- **Input Schema**:
  ```json
  {
    "sources": ["twitter", "techcrunch"],
    "lookback_hours": 24
  }
  ```
- **Output Schema**:
  ```json
  {
    "trends": [
      { "topic": "AI Agents", "score": 0.95, "url": "..." }
    ]
  }
  ```

### 2. `skill_write_script`
Generates a video script from a topic.
- **Input Schema**:
  ```json
  {
      "trend_context": {...},
      "duration_target": 60
  }
  ```
- **Output Schema**:
  ```json
  {
      "title": "...",
      "body": "...",
      "scenes": [ ... ]
  }
  ```

### 3. `skill_render_video`
Compiles assets into a final video.
- **Input Schema**:
  ```json
  {
      "script": {...},
      "voice_id": "alloy"
  }
  ```
- **Output Schema**:
  ```json
  {
      "video_path": "/data/renders/vid_123.mp4",
      "duration": 58
  }
  ```
