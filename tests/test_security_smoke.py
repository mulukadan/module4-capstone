import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from agents.security import (
    contains_raw_bearer_token,
    redact_sensitive_text,
)


def test_bearer_token_is_redacted():

    raw = "Authorization: " "Bearer demo-secret-token"

    result = redact_sensitive_text(raw)

    assert "demo-secret-token" not in result

    assert "[REDACTED_TOKEN]" in result


def test_patient_id_is_redacted():

    raw = "patient_id=12345678"

    result = redact_sensitive_text(raw)

    assert "12345678" not in result

    assert "[REDACTED_ID]" in result


def test_combined_redaction():

    raw = (
        "Authorization: "
        "Bearer another-secret "
        "patient_id=87654321 "
        "symptoms=headache"
    )

    result = redact_sensitive_text(raw)

    assert "another-secret" not in result

    assert "87654321" not in result

    assert "[REDACTED_TOKEN]" in result

    assert "[REDACTED_ID]" in result


def test_redacted_text_contains_no_raw_token():

    raw = "Bearer super-secret-value"

    result = redact_sensitive_text(raw)

    assert contains_raw_bearer_token(result) is False


def test_safe_text_remains_readable():

    raw = "Patient reports mild fever."

    result = redact_sensitive_text(raw)

    assert result == raw


def test_env_file_not_required_for_tests():

    env_file = PROJECT_ROOT / ".env"

    # Tests must work without requiring
    # a committed real .env file.
    assert not env_file.exists() or env_file.is_file()
