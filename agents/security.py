import re

BEARER_PATTERN = re.compile(
    r"Bearer\s+[A-Za-z0-9\-._~+/]+=*",
    re.IGNORECASE,
)


IDENTITY_PATTERN = re.compile(r"\b\d{7,10}\b")


def redact_sensitive_text(
    text: str,
) -> str:

    redacted = BEARER_PATTERN.sub(
        "[REDACTED_TOKEN]",
        text,
    )

    redacted = IDENTITY_PATTERN.sub(
        "[REDACTED_ID]",
        redacted,
    )

    return redacted


def contains_raw_bearer_token(
    text: str,
) -> bool:

    return bool(BEARER_PATTERN.search(text))


if __name__ == "__main__":

    sample = (
        "Authorization: "
        "Bearer demo-secret-token "
        "patient_id=12345678 "
        "symptoms=fever"
    )

    print(redact_sensitive_text(sample))
