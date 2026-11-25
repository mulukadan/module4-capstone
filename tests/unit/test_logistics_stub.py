import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from agents.logistics_stub import (
    check_stock,
)


def test_check_stock_returns_quantity():

    result = check_stock(
        clinic="Central Clinic",
        item="amoxicillin",
    )

    assert result["quantity"] == 40


def test_check_stock_returns_minimal_fields():

    result = check_stock(
        clinic="Central Clinic",
        item="amoxicillin",
    )

    assert set(result.keys()) == {
        "clinic",
        "item",
        "quantity",
    }


def test_unknown_clinic_rejected():

    with pytest.raises(ValueError):

        check_stock(
            clinic="Unknown Clinic",
            item="amoxicillin",
        )


def test_unknown_item_rejected():

    with pytest.raises(ValueError):

        check_stock(
            clinic="Central Clinic",
            item="unknown_item",
        )
