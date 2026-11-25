import sys
from pathlib import Path

import pytest
from fastapi.testclient import (
    TestClient,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from api.main import app

pytestmark = pytest.mark.integration


client = TestClient(app)


def test_health_returns_200():

    response = client.get("/health")

    assert response.status_code == 200


def test_health_reports_stub_mode():

    response = client.get("/health")

    body = response.json()

    assert body["status"] == "ok"

    assert body["mode"] == "stub"


def test_health_exposes_prompt_version():

    response = client.get("/health")

    body = response.json()

    assert body["prompt_version"] == "1.2.0"

    assert len(body["prompt_sha256"]) == 64
