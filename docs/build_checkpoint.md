# AfyaPlus Module 4 Capstone Build Checkpoint

## Checkpoint Status

The current AfyaPlus Module 4 Capstone has a working local Minimum Working Product in deterministic stub mode.

The core end-to-end path has been implemented and tested.

The project is not presented as a production clinical system.

---

## What Works

### 1. Project Definition

Present:

- `proposal.md`
- `skill_matrix.md`
- `integration_map.json`

The project path is the recommended AfyaPlus Module 4 Capstone.

Weeks 1 to 10 are mapped to final-capstone evidence.

---

### 2. Message Router

Implemented:

`agents/router.py`

Routes supported:

- emergency
- clinical
- logistics

Current behavior is deterministic and covered by unit tests.

---

### 3. Local Retrieval

Implemented:

`agents/retrieval.py`

Knowledge source:

`fixtures/knowledge_base.json`

The current retrieval twin uses token overlap.

It runs locally and deterministically.

---

### 4. Logistics Tool

Implemented:

`agents/logistics_stub.py`

Current tool:

`check_stock`

The tool returns a small structured result from local teaching fixtures.

No live production inventory system is queried.

---

### 5. FastAPI Service

Implemented:

`api/main.py`

Endpoints:

- `GET /health`
- `POST /triage`

The health endpoint has been manually verified over HTTP.

---

### 6. Authentication

JWT authentication is implemented for `/triage`.

Token claims include:

- subject
- role

Role restrictions are applied to clinical and logistics paths.

The demo uses a temporary runtime secret.

No real signing secret is committed.

---

### 7. Prompt Pinning

Prompt:

`prompts/triage_system_v1.2.0.txt`

Pin:

`prompts/pin.json`

Current version:

```text
1.2.0
```

Prompt hash verification passes.

The pin uses line-ending normalization for cross-platform consistency.

---

### 8. Security Redaction

Implemented:

`agents/security.py`

Smoke test:

`tests/test_security_smoke.py`

Current redaction evidence covers:

- raw Bearer tokens
- numeric identifiers
- combined sensitive strings

The raw values are removed from the redacted result.

---

### 9. Synthetic Fixtures

Primary fixture:

`fixtures/triage_messages_sample.jsonl`

Current row count:

```text
300
```

All rows are synthetic.

No production patient scrape is used.

SokoniHub catalog fixtures are not mixed with AfyaPlus clinical fixtures.

---

### 10. Golden Evaluation

Golden set:

`evals/golden.jsonl`

Runner:

`evals/run_eval.py`

Current result:

```text
10/10 correct
Score = 1.00
Threshold = 0.90
EVAL = PASSED
```

The score measures routing behavior on a small teaching set.

It is not a clinical-safety score.

---

### 11. Testing Pyramid

#### Default tests

```text
31 passed
```

Command:

```bash
pytest -q
```

#### Integration tests

```text
8 passed
```

Command:

```bash
pytest -q -m integration
```

#### Performance tests

```text
1 passed
```

Command:

```bash
pytest -q -m perf
```

A Starlette/httpx deprecation warning is currently visible, but it does not fail the suite.

The warning remains visible rather than being suppressed.

---

### 12. Performance Measurement

Script:

`scripts/measure_perf.py`

Output:

`perf_stub.json`

Current measured run:

```text
iterations = 1000
mean_ms = 0.001053
median_ms = 0.001000
p95_ms = 0.001100
max_ms = 0.006500
network_calls = 0
model_calls = 0
```

This measures only the local deterministic router on one local machine.

It is not a production latency claim.

---

### 13. Minimum Working Product

One-command demo:

```bash
python scripts/run_demo.py
```

Current final result:

```text
MINIMUM WORKING PRODUCT: PASSED
```

Exit code:

```text
0
```

The demo covers:

- prompt pin
- synthetic fixtures
- health route
- JWT authentication
- clinical route
- retrieval
- logistics tool
- emergency route
- redaction
- golden eval

Demo transcript:

`evidence/demo_transcript.txt`

---

### 14. CI Workflow

Workflow path:

`.github/workflows/ci.yml`

Configured checks include:

- prompt pin check
- default tests
- security smoke
- golden eval
- integration tests
- performance measurement
- performance tests

Local equivalents are passing.

GitHub-hosted CI status should be verified after the repository is pushed.

---

### 15. Documentation Completed

Completed documents:

- `docs/architecture.md`
- `docs/deployment.md`
- `docs/cost_analysis.md`
- `docs/user_guide.md`
- `docs/build_checkpoint.md`

Fixture documentation:

- `fixtures/README.md`

Incident evidence:

- `docs/incident_note.md`

Demo guide:

- `DEMO.md`

---

## What Is Deferred

The following items are deliberately not implemented as live production components.

### 1. Live LLM

No paid OpenAI or other hosted LLM is required by the automated path.

A deterministic router is used instead.

No claim is made that a live LLM powers the current MWP.

---

### 2. Production RAG

The current retrieval layer is a local teaching twin.

It does not use:

- embeddings
- vector database
- production document store
- production healthcare knowledge base

A production retrieval architecture would require separate evaluation.

---

### 3. Production MCP Server

The logistics path is implemented as a local MCP-style stub.

It is not connected to a live logistics or inventory backend.

---

### 4. Cloud Deployment

No production cloud deployment has been executed.

Cloud deployment steps in:

`docs/deployment.md`

are planning guidance only.

---

### 5. Production Secret Manager

The project does not currently use a live cloud secret manager.

Production deployment should use an approved managed secret service.

---

### 6. Production Audit Platform

The capstone includes security-redaction evidence but does not claim a complete centralized production audit-log platform.

---

### 7. Clinical Diagnosis

The system does not diagnose medical conditions.

It provides teaching routing and escalation behavior only.

Human clinical review remains required.

---

### 8. Real Patient Data

No real patient dataset is used.

No live patient system is scraped.

The fixtures are synthetic.

---

### 9. Large-Scale Performance

Current performance evidence measures only the local deterministic router.

The project has not been load-tested at production traffic volumes.

---

### 10. Formal Legal or Clinical Approval

No regulator, lawyer, clinician, DPO or security authority is claimed to have approved the system for production use.

Formal reviews would be required before a real deployment.

---

## Known Issues

### Starlette / httpx Warning

Current tests show a deprecation warning related to FastAPI/Starlette TestClient and `httpx`.

The warning does not currently fail tests.

Recommended future action:

- review dependency compatibility
- update through a tested dependency upgrade
- do not suppress the warning without understanding the cause

---

## Immediate Remaining Work

Before final submission:

1. verify `.github/workflows/ci.yml` is green on GitHub
2. complete Git feature-branch evidence
3. complete `docs/peer_review_checklist.md`
4. complete `review_log.md`
5. create `docs/presentation_outline.md`
6. create `docs/presentation.pdf`
7. complete final `README.md`
8. run final secret checks
9. verify all paths in `integration_map.json`
10. capture final test and eval evidence

---

## Current Summary

The local capstone MWP is working and evidence-backed.

Current verified technical evidence:

```text
31 default tests passed
8 integration tests passed
1 performance test passed
10/10 golden eval
300 synthetic fixtures
MWP PASSED
exit code 0
```

The remaining work is mainly repository process evidence, final documentation linking, CI verification and presentation preparation.