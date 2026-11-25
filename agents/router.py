from dataclasses import dataclass


@dataclass(frozen=True)
class RouteDecision:
    route: str
    reason: str


EMERGENCY_TERMS = {
    "cannot breathe",
    "difficulty breathing",
    "unconscious",
    "severe bleeding",
    "chest pain",
}


LOGISTICS_TERMS = {
    "stock",
    "amoxicillin",
    "ors",
    "malaria kits",
    "delivery",
    "supplies",
}


def normalize_text(
    text: str,
) -> str:

    return text.strip().lower()


def route_message(
    message: str,
) -> RouteDecision:

    normalized = normalize_text(message)

    if not normalized:

        return RouteDecision(
            route="clinical",
            reason=("Empty input defaults " "to clinical review."),
        )

    for term in EMERGENCY_TERMS:

        if term in normalized:

            return RouteDecision(
                route="emergency",
                reason=(f"Emergency term " f"matched: {term}"),
            )

    for term in LOGISTICS_TERMS:

        if term in normalized:

            return RouteDecision(
                route="logistics",
                reason=(f"Logistics term " f"matched: {term}"),
            )

    return RouteDecision(
        route="clinical",
        reason=("No emergency or logistics " "term matched."),
    )


if __name__ == "__main__":

    samples = [
        "I cannot breathe",
        "I have fever for two days",
        "Do we have amoxicillin in stock?",
    ]

    for sample in samples:

        result = route_message(sample)

        print(f"{sample!r} " f"-> {result.route} " f"({result.reason})")
