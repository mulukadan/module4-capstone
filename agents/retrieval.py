import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

KNOWLEDGE_FILE = PROJECT_ROOT / "fixtures" / "knowledge_base.json"


STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "for",
    "has",
    "have",
    "i",
    "is",
    "it",
    "my",
    "of",
    "the",
    "to",
    "with",
}


def load_knowledge_base() -> list[dict]:

    with open(
        KNOWLEDGE_FILE,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def tokenize(
    text: str,
) -> set[str]:

    tokens = re.findall(
        r"[a-z0-9]+",
        text.lower(),
    )

    return {token for token in tokens if token not in STOP_WORDS}


def score_match(
    query: str,
    document: dict,
) -> int:

    query_tokens = tokenize(query)

    document_text = document["topic"] + " " + document["text"]

    document_tokens = tokenize(document_text)

    return len(query_tokens & document_tokens)


def retrieve(
    query: str,
    top_k: int = 1,
) -> list[dict]:

    knowledge_base = load_knowledge_base()

    scored = []

    for document in knowledge_base:

        score = score_match(
            query,
            document,
        )

        scored.append(
            {
                "id": document["id"],
                "topic": document["topic"],
                "text": document["text"],
                "score": score,
            }
        )

    scored.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return scored[:top_k]


if __name__ == "__main__":

    query = "I have fever and headache"

    results = retrieve(
        query,
        top_k=2,
    )

    print(f"Query: {query}")

    for result in results:

        print(f"{result['id']} " f"topic={result['topic']} " f"score={result['score']}")

        print(result["text"])

        print()
