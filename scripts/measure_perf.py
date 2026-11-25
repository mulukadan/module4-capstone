import json
import statistics
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)

from agents.router import (
    route_message,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FILE = PROJECT_ROOT / "perf_stub.json"


SAMPLE_MESSAGES = [
    "I have fever for two days",
    "I cannot breathe",
    "Do we have amoxicillin in stock?",
    "I have a headache",
    "Check ORS stock",
]


def percentile(
    values: list[float],
    percentile_value: float,
) -> float:

    ordered = sorted(values)

    index = int(round(percentile_value * (len(ordered) - 1)))

    return ordered[index]


def measure_router(
    iterations: int = 1000,
) -> dict:

    durations_ms = []

    for index in range(iterations):

        message = SAMPLE_MESSAGES[index % len(SAMPLE_MESSAGES)]

        start = time.perf_counter()

        route_message(message)

        end = time.perf_counter()

        duration_ms = (end - start) * 1000

        durations_ms.append(duration_ms)

    result = {
        "mode": "stub",
        "component": ("agents.router.route_message"),
        "iterations": iterations,
        "mean_ms": round(
            statistics.mean(durations_ms),
            6,
        ),
        "median_ms": round(
            statistics.median(durations_ms),
            6,
        ),
        "p95_ms": round(
            percentile(
                durations_ms,
                0.95,
            ),
            6,
        ),
        "max_ms": round(
            max(durations_ms),
            6,
        ),
        "network_calls": 0,
        "model_calls": 0,
        "note": (
            "Local deterministic stub measurement only. "
            "Not a production latency claim."
        ),
    }

    return result


def main():

    result = measure_router()

    OUTPUT_FILE.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    print()
    print("=" * 70)
    print("AFYAPLUS STUB PERFORMANCE")
    print("=" * 70)

    print(f"Iterations: " f"{result['iterations']}")

    print(f"Mean: " f"{result['mean_ms']:.6f} ms")

    print(f"Median: " f"{result['median_ms']:.6f} ms")

    print(f"P95: " f"{result['p95_ms']:.6f} ms")

    print(f"Max: " f"{result['max_ms']:.6f} ms")

    print()

    print("Output: perf_stub.json")


if __name__ == "__main__":
    main()
