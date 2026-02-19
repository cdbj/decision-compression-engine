from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_decision():
    payload = {
        "goal": "grow revenue sustainably",
        "constraints": ["seasonal demand", "small team"],
        "bottleneck": "low conversion",
    }
    r = client.post("/decision", json=payload)
    assert r.status_code == 200
    assert r.json() == payload
