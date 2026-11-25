import sys
from pathlib import Path

import pytest
from fastapi.testclient import (
    TestClient,
)
from jose import jwt

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from api.main import app

pytestmark = pytest.mark.integration


TEST_SECRET = "integration-test-only-key"

ALGORITHM = "HS256"


client = TestClient(app)


def create_token(
    role: str,
) -> str:

    return jwt.encode(
        {
            "sub": "test-user",
            "role": role,
        },
        TEST_SECRET,
        algorithm=ALGORITHM,
    )


def auth_header(
    role: str,
) -> dict:

    token = create_token(role)

    return {"Authorization": (f"Bearer {token}")}


def test_triage_requires_auth():

    response = client.post(
        "/triage",
        json={"message": ("I have fever")},
    )

    assert response.status_code in {
        401,
        403,
    }


def test_clinical_route(
    monkeypatch,
):

    monkeypatch.setenv(
        "JWT_SECRET",
        TEST_SECRET,
    )

    response = client.post(
        "/triage",
        headers=auth_header("clinical_ops"),
        json={"message": ("I have fever " "for two days")},
    )

    assert response.status_code == 200

    body = response.json()

    assert body["route"] == "clinical"

    assert body["retrieval"][0]["topic"] == "fever"


def test_logistics_route(
    monkeypatch,
):

    monkeypatch.setenv(
        "JWT_SECRET",
        TEST_SECRET,
    )

    response = client.post(
        "/triage",
        headers=auth_header("dispatcher"),
        json={
            "message": ("Do we have " "amoxicillin in stock?"),
            "clinic": ("Central Clinic"),
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["route"] == "logistics"

    assert body["tool"] == "check_stock"

    assert body["result"]["quantity"] == 40


def test_clinical_role_cannot_use_logistics(
    monkeypatch,
):

    monkeypatch.setenv(
        "JWT_SECRET",
        TEST_SECRET,
    )

    response = client.post(
        "/triage",
        headers=auth_header("clinical_ops"),
        json={"message": ("Check amoxicillin stock")},
    )

    assert response.status_code == 403


def test_emergency_route(
    monkeypatch,
):

    monkeypatch.setenv(
        "JWT_SECRET",
        TEST_SECRET,
    )

    response = client.post(
        "/triage",
        headers=auth_header("clinical_ops"),
        json={"message": ("I cannot breathe")},
    )

    assert response.status_code == 200

    body = response.json()

    assert body["route"] == "emergency"

    assert body["action"] == "urgent-human-review"
