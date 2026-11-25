import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FILE = PROJECT_ROOT / "fixtures" / "triage_messages_sample.jsonl"


TEMPLATES = [
    {
        "message": "I have fever for two days",
        "expected_route": "clinical",
    },
    {
        "message": "I have a severe headache",
        "expected_route": "clinical",
    },
    {
        "message": "I have been coughing since yesterday",
        "expected_route": "clinical",
    },
    {
        "message": "I have diarrhea and feel weak",
        "expected_route": "clinical",
    },
    {
        "message": "I cannot breathe",
        "expected_route": "emergency",
    },
    {
        "message": "I have chest pain",
        "expected_route": "emergency",
    },
    {
        "message": "Patient is unconscious",
        "expected_route": "emergency",
    },
    {
        "message": "Do we have amoxicillin in stock?",
        "expected_route": "logistics",
    },
    {
        "message": "Check ORS stock",
        "expected_route": "logistics",
    },
    {
        "message": "What malaria kits are in stock?",
        "expected_route": "logistics",
    },
]


def generate_rows(
    total_rows: int = 300,
) -> list[dict]:

    rows = []

    for index in range(total_rows):

        template = TEMPLATES[index % len(TEMPLATES)]

        row = {
            "fixture_id": (f"TRIAGE-{index + 1:03d}"),
            "message": (template["message"]),
            "expected_route": (template["expected_route"]),
            "synthetic": True,
        }

        rows.append(row)

    return rows


def main():

    rows = generate_rows(total_rows=300)

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        for row in rows:

            file.write(json.dumps(row) + "\n")

    print(f"Generated {len(rows)} " "synthetic triage rows.")

    print("Output: " "fixtures/" "triage_messages_sample.jsonl")


if __name__ == "__main__":
    main()
