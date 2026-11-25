import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from scripts.run_demo import (
    count_fixture_rows,
    load_pin,
)


def test_demo_fixture_count():

    assert count_fixture_rows() == 300


def test_demo_loads_prompt_pin():

    pin = load_pin()

    assert pin["prompt_version"] == "1.2.0"

    assert len(pin["sha256"]) == 64
