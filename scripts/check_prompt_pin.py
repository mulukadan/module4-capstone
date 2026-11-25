import json
import sys
from pathlib import Path

from build_prompt_pin import (
    calculate_sha256,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROMPT_FILE = PROJECT_ROOT / "prompts" / "triage_system_v1.2.0.txt"

PIN_FILE = PROJECT_ROOT / "prompts" / "pin.json"


def load_pin() -> dict:

    return json.loads(PIN_FILE.read_text(encoding="utf-8"))


def main():

    pin = load_pin()

    actual_sha = calculate_sha256(PROMPT_FILE)

    expected_sha = pin["sha256"]

    print(f"Expected: {expected_sha}")

    print(f"Actual:   {actual_sha}")

    if actual_sha != expected_sha:

        print("PROMPT PIN CHECK: FAILED")

        sys.exit(1)

    print("PROMPT PIN CHECK: PASSED")

    sys.exit(0)


if __name__ == "__main__":
    main()
