import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT),
)


from agents.retrieval import (
    load_knowledge_base,
    retrieve,
    tokenize,
)


def test_knowledge_base_loads():

    knowledge = load_knowledge_base()

    assert len(knowledge) >= 5


def test_tokenize_lowercases():

    tokens = tokenize("FEVER and Headache")

    assert "fever" in tokens
    assert "headache" in tokens


def test_fever_query_returns_fever():

    results = retrieve(
        "I have fever",
        top_k=1,
    )

    assert results[0]["topic"] == "fever"


def test_headache_query_returns_headache():

    results = retrieve(
        "severe headache",
        top_k=1,
    )

    assert results[0]["topic"] == "headache"


def test_retrieve_respects_top_k():

    results = retrieve(
        "fever headache cough",
        top_k=2,
    )

    assert len(results) == 2
