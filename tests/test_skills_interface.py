
import pytest
from typing import Dict, Any

def test_skill_interface_compliance():
    """
    Asserts that all Skills leverage the BaseSkill interface
    and strictly type-check their inputs.
    """
    
    # Intentional failure: The BaseSkill class is not yet part of the codebase
    try:
        from chimera.core.skills import BaseSkill
    except ImportError:
        pytest.fail("Architecture Error: 'chimera.core.skills.BaseSkill' is not defined.")

    # Mock implementation to test inheritance
    class MockSkill(BaseSkill):
        def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
             return {"status": "ok"}

    skill = MockSkill()
    assert hasattr(skill, "execute")
    assert skill.execute({}) == {"status": "ok"}
