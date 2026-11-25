# AfyaPlus Module 4 Capstone Cost Analysis

## Overview

The capstone is designed to run at near-zero cost in automated tests.

The default path uses:

- deterministic routing
- local fixtures
- local retrieval
- local logistics stub
- local prompt hashing
- local evaluation
- no paid model calls

This keeps CI reproducible and prevents automated tests from creating API charges.

---

## Teaching Cost Table

| Activity | Approximate calls | Estimated cost | Notes |
|---|---:|---:|---|
| Unit tests | 0 paid API calls | $0.00 | Local deterministic tests |
| Integration tests | 0 paid API calls | $0.00 | FastAPI TestClient |
| Performance test | 0 paid API calls | $0.00 | Local router measurement |
| Golden-set eval | 0 paid API calls | $0.00 | Deterministic router |
| Prompt pin check | 0 paid API calls | $0.00 | SHA-256 |
| MWP demo | 0 paid API calls | $0.00 | Local stub mode |
| Optional live Thursday demo | ~10 model calls | up to about $1.00 | Only if explicitly enabled |
| Typical automated capstone run | 0 paid calls | $0.00 | Default path |

---

## Assumptions

The cost table assumes:

- local Python execution
- no paid hosted LLM in automated tests
- no production database
- no hosted vector database
- no cloud deployment
- local FastAPI execution
- synthetic fixtures only

The optional live model cost is a teaching estimate rather than a billing guarantee.

Actual provider prices may change.

---

## Cost-Control Design

The project applies several cost-control practices.

### Stub First

Tests use deterministic implementations.

This avoids:

- accidental API spending
- flaky responses
- variable latency
- rate-limit failures

### Small Golden Set

The golden set contains:

```text
10 labelled cases
```

This is sufficient for teaching regression evidence without making unnecessary paid calls.

### Controlled Fixture Size

The main teaching fixture contains:

```text
300 synthetic rows
```

The project intentionally avoids millions of rows.

### Local Retrieval

The current retrieval twin uses local token overlap.

It does not require:

- embedding API calls
- a hosted vector database
- external search calls

### Local MCP Stub

The current `check_stock` tool uses local fixture data.

It makes:

```text
0 network calls
```

during tests.

---

## Measured Performance Evidence

Performance result:

`perf_stub.json`

The current measurement covers:

`agents.router.route_message`

Current run:

```text
iterations = 1000
mean_ms = 0.001053
median_ms = 0.001000
p95_ms = 0.001100
max_ms = 0.006500
network_calls = 0
model_calls = 0
```

These numbers are from one local machine and measure only the deterministic router.

They must not be presented as production service latency.

---

## Production Cost Drivers

If the system later moves beyond stub mode, likely cost drivers include:

- hosted LLM tokens
- embedding generation
- vector-database storage and queries
- cloud compute
- logging and monitoring
- managed secret services
- data storage
- network traffic
- backup and recovery

---

## Recommended Production Cost Controls

Before enabling paid services:

1. measure request volume
2. estimate token use
3. cache repeat retrieval results where appropriate
4. batch suitable background operations
5. enforce maximum prompt and response sizes
6. monitor cost per request
7. set provider budgets and alerts
8. keep deterministic tests separate from paid live tests

---

## What This Analysis Does Not Claim

This document does not claim:

- production cost accuracy
- fixed future API pricing
- cloud-hosting cost certainty
- production traffic forecasts

The values are teaching estimates based on the current stub-first capstone design.