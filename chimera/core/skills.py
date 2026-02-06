from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseSkill(ABC):
    """Base class for all Chimera skills.

    Skills must implement the execute method and accept/return
    plain dictionaries that will be validated against schemas
    defined in the specs.
    """

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:  # pragma: no cover - interface only
        """Run the skill logic for a given payload."""
        raise NotImplementedError
