from __future__ import annotations

import json
from decision_engine import generate_decision_brief


def _read_constraints() -> list[str]:
    print("Enter constraints (one per line). Empty line to finish:")
    items: list[str] = []
    while True:
        line = input("> ").strip()
        if line == "":
            break
        items.append(line)
    return items


def main() -> None:
    goal = input("Goal (one sentence): ").strip()
    constraints = _read_constraints()
    bottleneck = input("Current bottleneck: ").strip()

    brief = generate_decision_brief(goal=goal, constraints=constraints, bottleneck=bottleneck)
    print("\n--- Decision Brief (JSON) ---")
    print(json.dumps(brief.to_dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
    