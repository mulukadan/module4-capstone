import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from agents.router import (
    route_message,
)

GOLDEN_FILE = PROJECT_ROOT / "evals" / "golden.jsonl"


PASS_THRESHOLD = 0.90


def load_golden_set() -> list[dict]:

    rows = []

    with open(
        GOLDEN_FILE,
        "r",
        encoding="utf-8",
    ) as file:

        for line in file:

            line = line.strip()

            if line:

                rows.append(json.loads(line))

    return rows


def run_eval() -> dict:

    cases = load_golden_set()

    passed = 0
    results = []

    for case in cases:

        decision = route_message(case["message"])

        actual = decision.route

        correct = actual == case["expected_route"]

        if correct:
            passed += 1

        results.append(
            {
                "id": case["id"],
                "expected": (case["expected_route"]),
                "actual": actual,
                "passed": correct,
            }
        )

    total = len(cases)

    score = passed / total if total else 0.0

    return {
        "passed": passed,
        "total": total,
        "score": score,
        "threshold": (PASS_THRESHOLD),
        "results": results,
    }


def main():

    report = run_eval()

    print()
    print("=" * 70)
    print("AFYAPLUS GOLDEN-SET EVAL")
    print("=" * 70)

    for result in report["results"]:

        status = "PASS" if result["passed"] else "FAIL"

        print(
            f"{result['id']} "
            f"expected="
            f"{result['expected']} "
            f"actual="
            f"{result['actual']} "
            f"{status}"
        )

    print()

    print(
        f"Score: "
        f"{report['passed']}/"
        f"{report['total']} "
        f"= "
        f"{report['score']:.2f}"
    )

    print(f"Threshold: " f"{report['threshold']:.2f}")

    if report["score"] < report["threshold"]:

        print("EVAL: FAILED")

        sys.exit(1)

    print("EVAL: PASSED")

    sys.exit(0)


if __name__ == "__main__":
    main()
