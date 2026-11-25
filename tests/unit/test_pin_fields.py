import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from scripts.build_prompt_pin import (
    calculate_sha256,
)

PIN_FILE = PROJECT_ROOT / "prompts" / "pin.json"

PROMPT_FILE = PROJECT_ROOT / "prompts" / "triage_system_v1.2.0.txt"


def load_pin():

    return json.loads(PIN_FILE.read_text(encoding="utf-8"))


def test_pin_has_prompt_file():

    pin = load_pin()

    assert pin["prompt_file"] == ("prompts/" "triage_system_v1.2.0.txt")


def test_pin_has_version():

    pin = load_pin()

    assert pin["prompt_version"] == "1.2.0"


def test_pin_has_sha256():

    pin = load_pin()

    assert len(pin["sha256"]) == 64


def test_pin_uses_lf_normalization():

    pin = load_pin()

    assert pin["normalization"] == "lf"


def test_pin_matches_prompt():

    pin = load_pin()

    actual_sha = calculate_sha256(PROMPT_FILE)

    assert actual_sha == pin["sha256"]
