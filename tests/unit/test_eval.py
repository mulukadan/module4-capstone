import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from evals.run_eval import (
    run_eval,
)


def test_golden_eval_meets_threshold():

    report = run_eval()

    assert report["score"] >= report["threshold"]


def test_golden_eval_has_ten_cases():

    report = run_eval()

    assert report["total"] == 10


def test_golden_eval_all_pass():

    report = run_eval()

    assert report["passed"] == 10
