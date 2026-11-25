import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from scripts.measure_perf import (
    measure_router,
)

pytestmark = pytest.mark.perf


def test_router_perf_stub_runs():

    result = measure_router(iterations=100)

    assert result["iterations"] == 100

    assert result["network_calls"] == 0

    assert result["model_calls"] == 0

    assert result["p95_ms"] >= 0
