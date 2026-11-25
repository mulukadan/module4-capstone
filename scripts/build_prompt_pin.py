import hashlib
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROMPT_FILE = PROJECT_ROOT / "prompts" / "triage_system_v1.2.0.txt"

PIN_FILE = PROJECT_ROOT / "prompts" / "pin.json"


def normalized_text(
    file_path: Path,
) -> str:

    text = file_path.read_text(encoding="utf-8")

    return text.replace("\r\n", "\n").replace("\r", "\n")


def calculate_sha256(
    file_path: Path,
) -> str:

    text = normalized_text(file_path)

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_pin() -> dict:

    sha256 = calculate_sha256(PROMPT_FILE)

    pin = {
        "prompt_file": ("prompts/" "triage_system_v1.2.0.txt"),
        "prompt_version": "1.2.0",
        "sha256": sha256,
        "normalization": "lf",
    }

    PIN_FILE.write_text(
        json.dumps(
            pin,
            indent=2,
        ),
        encoding="utf-8",
    )

    return pin


if __name__ == "__main__":

    pin = build_pin()

    print("PROMPT PIN GENERATED")

    print(f"Version: " f"{pin['prompt_version']}")

    print(f"SHA-256: " f"{pin['sha256']}")
