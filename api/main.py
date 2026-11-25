import json
import os
from pathlib import Path

from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
)
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from jose import (
    JWTError,
    jwt,
)
from pydantic import BaseModel

from agents.logistics_stub import (
    VALID_ITEMS,
    check_stock,
)
from agents.retrieval import retrieve
from agents.router import route_message

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PIN_FILE = PROJECT_ROOT / "prompts" / "pin.json"


ALGORITHM = "HS256"

security = HTTPBearer()


app = FastAPI(
    title="AfyaPlus Module 4 Capstone",
    version="1.0.0",
)


class TriageRequest(BaseModel):
    message: str
    clinic: str = "Central Clinic"


def load_prompt_pin() -> dict:

    return json.loads(PIN_FILE.read_text(encoding="utf-8"))


def get_jwt_secret() -> str:

    secret = os.getenv("JWT_SECRET")

    if not secret:

        raise HTTPException(
            status_code=500,
            detail=("JWT_SECRET is not configured."),
        )

    return secret


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            get_jwt_secret(),
            algorithms=[ALGORITHM],
        )

    except JWTError as exc:

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        ) from exc

    user_id = payload.get("sub")

    role = payload.get("role")

    if not user_id or not role:

        raise HTTPException(
            status_code=401,
            detail=("Token missing required claims"),
        )

    return {
        "user_id": user_id,
        "role": role,
    }


def detect_stock_item(
    message: str,
) -> str | None:

    normalized = message.lower().replace(" ", "_")

    for item in VALID_ITEMS:

        if (
            item in normalized
            or item.replace(
                "_",
                " ",
            )
            in message.lower()
        ):

            return item

    return None


@app.get("/health")
def health():

    pin = load_prompt_pin()

    return {
        "status": "ok",
        "service": ("afyaplus-module4-capstone"),
        "mode": "stub",
        "prompt_version": (pin["prompt_version"]),
        "prompt_sha256": (pin["sha256"]),
    }


@app.post("/triage")
def triage(
    request: TriageRequest,
    user: dict = Depends(get_current_user),
):

    decision = route_message(request.message)

    if decision.route == "emergency":

        return {
            "route": "emergency",
            "action": ("urgent-human-review"),
            "message": (
                "Emergency indicators " "were detected. Seek " "urgent clinical review."
            ),
        }

    if decision.route == "logistics":

        if user["role"] not in {
            "dispatcher",
            "platform_admin",
        }:

            raise HTTPException(
                status_code=403,
                detail=("Role not allowed " "for logistics tools"),
            )

        item = detect_stock_item(request.message)

        if item is None:

            raise HTTPException(
                status_code=400,
                detail=("No supported stock " "item found in message"),
            )

        stock = check_stock(
            clinic=request.clinic,
            item=item,
        )

        return {
            "route": "logistics",
            "tool": "check_stock",
            "result": stock,
        }

    if user["role"] not in {
        "clinical_ops",
        "platform_admin",
    }:

        raise HTTPException(
            status_code=403,
            detail=("Role not allowed " "for clinical triage"),
        )

    knowledge = retrieve(
        request.message,
        top_k=1,
    )

    return {
        "route": "clinical",
        "retrieval": knowledge,
        "action": "clinical-review",
    }
