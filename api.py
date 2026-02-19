from __future__ import annotations

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

from decision_engine import generate_decision_brief

app = FastAPI(title="DCE API", version="0.1.0")


class DecisionRequest(BaseModel):
    goal: str = Field(default="")
    constraints: List[str] = Field(default_factory=list)
    bottleneck: str = Field(default="")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/decision")
def decision(req: DecisionRequest) -> dict:
    brief = generate_decision_brief(
        goal=req.goal,
        constraints=req.constraints,
        bottleneck=req.bottleneck,
    )
    return brief.to_dict()
