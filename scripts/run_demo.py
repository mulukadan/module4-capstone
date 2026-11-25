import json
import os
import secrets
import sys
from pathlib import Path

from fastapi.testclient import TestClient
from jose import jwt

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from agents.security import (
    redact_sensitive_text,
)
from api.main import app
from evals.run_eval import (
    run_eval,
)
from scripts.build_prompt_pin import (
    calculate_sha256,
)

PROMPT_FILE = PROJECT_ROOT / "prompts" / "triage_system_v1.2.0.txt"

PIN_FILE = PROJECT_ROOT / "prompts" / "pin.json"

FIXTURE_FILE = PROJECT_ROOT / "fixtures" / "triage_messages_sample.jsonl"

TRANSCRIPT_FILE = PROJECT_ROOT / "evidence" / "demo_transcript.txt"


ALGORITHM = "HS256"


def emit(
    lines: list[str],
    text: str = "",
):

    print(text)
    lines.append(text)


def load_pin() -> dict:

    return json.loads(PIN_FILE.read_text(encoding="utf-8"))


def count_fixture_rows() -> int:

    with open(
        FIXTURE_FILE,
        "r",
        encoding="utf-8",
    ) as file:

        return sum(1 for line in file if line.strip())


def create_token(
    secret: str,
    role: str,
) -> str:

    return jwt.encode(
        {
            "sub": "demo-user",
            "role": role,
        },
        secret,
        algorithm=ALGORITHM,
    )


def main():

    lines = []

    # A new random secret is generated only for
    # this demo process. Nothing is committed.
    demo_secret = secrets.token_urlsafe(32)

    os.environ["JWT_SECRET"] = demo_secret

    client = TestClient(app)

    emit(
        lines,
        "=" * 70,
    )

    emit(
        lines,
        "AFYAPLUS MODULE 4 CAPSTONE DEMO",
    )

    emit(
        lines,
        "=" * 70,
    )

    # ------------------------------------------------
    # 1. Prompt pin
    # ------------------------------------------------

    pin = load_pin()

    actual_sha = calculate_sha256(PROMPT_FILE)

    pin_ok = actual_sha == pin["sha256"]

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "1. PROMPT PIN",
    )

    emit(
        lines,
        ("Version: " f"{pin['prompt_version']}"),
    )

    emit(
        lines,
        ("SHA match: " f"{pin_ok}"),
    )

    # ------------------------------------------------
    # 2. Fixtures
    # ------------------------------------------------

    fixture_count = count_fixture_rows()

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "2. SYNTHETIC FIXTURES",
    )

    emit(
        lines,
        ("Rows: " f"{fixture_count}"),
    )

    emit(
        lines,
        "Production scrape: False",
    )

    # ------------------------------------------------
    # 3. Health
    # ------------------------------------------------

    health_response = client.get("/health")

    health_body = health_response.json()

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "3. HEALTH",
    )

    emit(
        lines,
        ("HTTP status: " f"{health_response.status_code}"),
    )

    emit(
        lines,
        ("Mode: " f"{health_body['mode']}"),
    )

    emit(
        lines,
        ("Prompt version: " f"{health_body['prompt_version']}"),
    )

    # ------------------------------------------------
    # 4. Clinical + retrieval
    # ------------------------------------------------

    clinical_token = create_token(
        demo_secret,
        "clinical_ops",
    )

    clinical_response = client.post(
        "/triage",
        headers={"Authorization": ("Bearer " + clinical_token)},
        json={"message": ("I have fever " "for two days")},
    )

    clinical_body = clinical_response.json()

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "4. CLINICAL + RAG",
    )

    emit(
        lines,
        ("HTTP status: " f"{clinical_response.status_code}"),
    )

    emit(
        lines,
        ("Route: " f"{clinical_body['route']}"),
    )

    emit(
        lines,
        ("Retrieved topic: " f"{clinical_body['retrieval'][0]['topic']}"),
    )

    # ------------------------------------------------
    # 5. Logistics MCP-style tool
    # ------------------------------------------------

    dispatcher_token = create_token(
        demo_secret,
        "dispatcher",
    )

    logistics_response = client.post(
        "/triage",
        headers={"Authorization": ("Bearer " + dispatcher_token)},
        json={
            "message": ("Do we have " "amoxicillin in stock?"),
            "clinic": ("Central Clinic"),
        },
    )

    logistics_body = logistics_response.json()

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "5. LOGISTICS TOOL",
    )

    emit(
        lines,
        ("HTTP status: " f"{logistics_response.status_code}"),
    )

    emit(
        lines,
        ("Route: " f"{logistics_body['route']}"),
    )

    emit(
        lines,
        ("Tool: " f"{logistics_body['tool']}"),
    )

    emit(
        lines,
        ("Quantity: " f"{logistics_body['result']['quantity']}"),
    )

    # ------------------------------------------------
    # 6. Emergency path
    # ------------------------------------------------

    emergency_response = client.post(
        "/triage",
        headers={"Authorization": ("Bearer " + clinical_token)},
        json={"message": ("I cannot breathe")},
    )

    emergency_body = emergency_response.json()

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "6. EMERGENCY PATH",
    )

    emit(
        lines,
        ("Route: " f"{emergency_body['route']}"),
    )

    emit(
        lines,
        ("Action: " f"{emergency_body['action']}"),
    )

    # ------------------------------------------------
    # 7. Security redaction
    # ------------------------------------------------

    sensitive_sample = (
        "Authorization: "
        "Bearer demo-secret-token "
        "patient_id=12345678 "
        "symptoms=fever"
    )

    redacted = redact_sensitive_text(sensitive_sample)

    redaction_ok = "demo-secret-token" not in redacted and "12345678" not in redacted

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "7. SECURITY REDACTION",
    )

    emit(
        lines,
        redacted,
    )

    emit(
        lines,
        ("Redaction passed: " f"{redaction_ok}"),
    )

    # ------------------------------------------------
    # 8. Golden eval
    # ------------------------------------------------

    eval_report = run_eval()

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "8. GOLDEN EVAL",
    )

    emit(
        lines,
        (
            "Score: "
            f"{eval_report['passed']}/"
            f"{eval_report['total']} "
            f"= "
            f"{eval_report['score']:.2f}"
        ),
    )

    emit(
        lines,
        ("Threshold: " f"{eval_report['threshold']:.2f}"),
    )

    # ------------------------------------------------
    # Final assertions
    # ------------------------------------------------

    checks = [
        pin_ok,
        fixture_count == 300,
        health_response.status_code == 200,
        clinical_response.status_code == 200,
        clinical_body["route"] == "clinical",
        logistics_response.status_code == 200,
        logistics_body["tool"] == "check_stock",
        emergency_body["route"] == "emergency",
        redaction_ok,
        eval_report["score"] >= eval_report["threshold"],
    ]

    passed = all(checks)

    emit(
        lines,
        "",
    )

    emit(
        lines,
        "=" * 70,
    )

    emit(
        lines,
        ("MINIMUM WORKING PRODUCT: " + ("PASSED" if passed else "FAILED")),
    )

    emit(
        lines,
        "=" * 70,
    )

    TRANSCRIPT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    TRANSCRIPT_FILE.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    print()
    print("Transcript written to " "evidence/demo_transcript.txt")

    if not passed:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
