from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class DecisionBrief:
    goal: str
    constraints: List[str]
    bottleneck: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def generate_decision_brief(goal: str, constraints: List[str], bottleneck: str) -> DecisionBrief:
    goal = (goal or "").strip()
    bottleneck = (bottleneck or "").strip()
    constraints = [c.strip() for c in (constraints or []) if c and c.strip()]

    return DecisionBrief(
        goal=goal,
        constraints=constraints,
        bottleneck=bottleneck,
    )
