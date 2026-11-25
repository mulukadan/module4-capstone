import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from agents.router import (
    RouteDecision,
    normalize_text,
    route_message,
)


def test_normalize_text():

    result = normalize_text("  CHEST PAIN  ")

    assert result == "chest pain"


def test_emergency_route():

    result = route_message("Patient has difficulty breathing")

    assert isinstance(
        result,
        RouteDecision,
    )

    assert result.route == "emergency"


def test_clinical_route():

    result = route_message("I have had fever for two days")

    assert result.route == "clinical"


def test_logistics_route():

    result = route_message("Do we have amoxicillin in stock?")

    assert result.route == "logistics"


def test_unknown_message_defaults_to_clinical():

    result = route_message("I feel tired today")

    assert result.route == "clinical"


def test_empty_message_defaults_to_clinical():

    result = route_message("   ")

    assert result.route == "clinical"
