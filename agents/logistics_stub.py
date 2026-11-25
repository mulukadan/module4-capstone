STOCK_FIXTURE = {
    "Central Clinic": {
        "amoxicillin": 40,
        "ors_sachets": 120,
        "malaria_kits": 20,
    },
    "East Clinic": {
        "amoxicillin": 15,
        "ors_sachets": 60,
        "malaria_kits": 8,
    },
}


VALID_ITEMS = {
    "amoxicillin",
    "ors_sachets",
    "malaria_kits",
}


def check_stock(
    clinic: str,
    item: str,
) -> dict:

    if clinic not in STOCK_FIXTURE:
        raise ValueError(f"Unknown clinic: {clinic}")

    if item not in VALID_ITEMS:
        raise ValueError(f"Unsupported item: {item}")

    quantity = STOCK_FIXTURE[clinic][item]

    return {
        "clinic": clinic,
        "item": item,
        "quantity": quantity,
    }


if __name__ == "__main__":

    result = check_stock(
        clinic="Central Clinic",
        item="amoxicillin",
    )

    print(result)
