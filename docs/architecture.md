# AfyaPlus Module 4 Capstone Architecture

## Overview

The AfyaPlus Module 4 Capstone integrates selected engineering practices from Weeks 1 to 10 into one deterministic health-operations teaching system.

The Minimum Working Product includes:

- FastAPI service
- JWT authentication
- deterministic routing
- local RAG-style retrieval
- logistics MCP-style stub tool
- prompt pinning
- security redaction
- golden-set evaluation
- synthetic fixtures
- performance measurement
- automated tests

The automated path uses deterministic local stubs so it can run without paid model APIs or production infrastructure.

---

## System Flow

```text
Client
  |
  v
FastAPI
  |
  v
JWT Authentication
  |
  v
Message Router
  |
  +----------------+----------------+
  |                |                |
  v                v                v
Emergency       Clinical         Logistics
  |                |                |
  v                v                v
Human review   Retrieval       check_stock()
               RAG twin        MCP-style stub
```

---

## API Layer

Implementation:

`api/main.py`

The API exposes:

### GET /health

Returns:

- service status
- execution mode
- prompt version
- prompt SHA-256

The health endpoint provides runtime evidence that the configured prompt pin is connected to the application.

### POST /triage

Accepts a message and optional clinic name.

The request requires JWT authentication.

The route may return:

- emergency escalation
- clinical retrieval
- logistics tool output

---

## Authentication

JWT authentication uses:

`python-jose`

The API expects:

- `sub`
- `role`

Supported teaching roles include:

- `clinical_ops`
- `dispatcher`
- `platform_admin`

The JWT signing secret is read from:

`JWT_SECRET`

The secret is not stored in source code.

The demo script creates a temporary runtime secret and does not write it to disk.

---

## Router

Implementation:

`agents/router.py`

The router classifies messages into:

- `emergency`
- `clinical`
- `logistics`

The current implementation is deterministic and keyword-based.

This is intentionally a teaching stub.

It is not presented as a production AI classifier.

---

## Clinical Retrieval

Implementation:

`agents/retrieval.py`

Knowledge source:

`fixtures/knowledge_base.json`

The retrieval layer:

1. tokenizes the query
2. tokenizes local knowledge records
3. scores token overlap
4. returns the best matching record

This is a local RAG-style teaching twin.

It does not use:

- a vector database
- embeddings
- a live LLM

A production system could replace this implementation with an embedding-based retrieval layer after evaluation.

---

## Logistics MCP-Style Tool

Implementation:

`agents/logistics_stub.py`

Current tool:

`check_stock`

The tool reads from a local teaching inventory fixture.

Example:

```text
Clinic: Central Clinic
Item: amoxicillin
Quantity: 40
```

The tool is deterministic and does not connect to a production inventory system.

---

## Prompt Pinning

Prompt:

`prompts/triage_system_v1.2.0.txt`

Pin:

`prompts/pin.json`

Pin generator:

`scripts/build_prompt_pin.py`

Pin checker:

`scripts/check_prompt_pin.py`

The prompt SHA-256 is normalized to LF line endings before hashing.

This avoids false pin mismatches between Windows and Linux environments.

---

## Security

Implementation:

`agents/security.py`

Security smoke:

`tests/test_security_smoke.py`

Current controls include:

- Bearer-token redaction
- numeric identifier redaction
- secret exclusion through `.gitignore`
- JWT authentication
- role restrictions for clinical and logistics paths
- deterministic stub mode for automated tests

Security controls are teaching evidence and are not described as complete production security.

---

## Evaluation

Golden set:

`evals/golden.jsonl`

Runner:

`evals/run_eval.py`

Current evidence:

```text
10/10 correct
Score = 1.00
Threshold = 0.90
```

The evaluation measures route classification on the labelled teaching set.

It is not a medical-quality or clinical-safety benchmark.

---

## Fixtures

Primary fixture:

`fixtures/triage_messages_sample.jsonl`

Current size:

```text
300 synthetic rows
```

The fixture is generated locally.

It contains no production patient records.

SokoniHub catalog fixtures are not mixed into the AfyaPlus fixture set.

---

## Performance

Measurement script:

`scripts/measure_perf.py`

Output:

`perf_stub.json`

The measurement covers only:

`agents.router.route_message`

Current performance measurements therefore represent local deterministic stub latency only.

They are not production API latency claims.

---

## Testing Pyramid

### Default / Unit

Command:

```bash
pytest -q
```

Current result:

```text
31 passed
```

### Integration

Command:

```bash
pytest -q -m integration
```

Current result:

```text
8 passed
```

### Performance

Command:

```bash
pytest -q -m perf
```

Current result:

```text
1 passed
```

---

## Minimum Working Product

Command:

```bash
python scripts/run_demo.py
```

The MWP demonstrates:

- prompt pin verification
- synthetic fixture count
- health endpoint
- JWT authentication
- clinical routing
- retrieval
- logistics tool
- emergency escalation
- security redaction
- golden-set evaluation

A successful run ends with:

```text
MINIMUM WORKING PRODUCT: PASSED
```

---

## Deferred Production Components

The following are not implemented as live production services:

- production patient database
- live vector database
- hosted LLM
- production MCP server
- cloud secret manager
- cloud deployment
- medical diagnosis engine

These are intentionally deferred and are not claimed as complete.