# Module 4 Capstone: AfyaPlus

## Overview

This repository contains the AfyaPlus Module 4 Capstone, an integrated teaching system that brings together engineering practices from Weeks 1 to 10.

The Minimum Working Product combines:

- FastAPI
- JWT authentication
- deterministic triage routing
- local RAG-style retrieval
- logistics MCP-style tooling
- prompt/version pinning
- security redaction
- synthetic fixtures
- golden-set evaluation
- performance measurement
- automated testing
- CI/CD evidence
- responsible deployment documentation

The project runs in deterministic stub mode by default and does not require a paid model API.

It is a teaching system and is not presented as a production clinical or diagnostic system.

---

## Project Path

- [x] AfyaPlus Module 4 Capstone — recommended path
- [ ] Domain / field alternative

---

## Week Reuse

### Weeks 1–5

Reused concepts:

- LLM fundamentals
- prompt design
- retrieval and RAG concepts
- embeddings/vector retrieval concepts
- multimodal design principles

Final evidence includes the local retrieval twin and architecture documentation.

### Week 6

Reused:

- FastAPI
- `/health`
- `/triage`
- authenticated API behavior

Final implementation:

`api/main.py`

### Week 7

Reused:

- logistics tool concepts
- MCP-style tool path
- performance measurement
- cost-analysis habits

Evidence:

- `agents/logistics_stub.py`
- `scripts/measure_perf.py`
- `perf_stub.json`
- `docs/cost_analysis.md`

### Week 8

Reused:

- prompt pinning
- SHA-256 verification
- golden-set evaluation
- CI gating

Evidence:

- `prompts/triage_system_v1.2.0.txt`
- `prompts/pin.json`
- `scripts/check_prompt_pin.py`
- `evals/golden.jsonl`
- `evals/run_eval.py`
- `.github/workflows/ci.yml`

### Week 9

Reused:

- security hygiene
- authentication
- access control
- redaction
- no-secret Git practices

Evidence:

- `agents/security.py`
- `tests/test_security_smoke.py`
- `.gitignore`

### Week 10

Reused:

- provenance and honesty practices
- strict separation of data domains
- explicit fallback declarations

SokoniHub retail fixtures are not mixed with AfyaPlus clinical fixtures.

---

## Project Structure

```text
module4-capstone/
│
├── README.md
├── DEMO.md
├── proposal.md
├── skill_matrix.md
├── integration_map.json
├── requirements.txt
├── pytest.ini
├── perf_stub.json
│
├── agents/
│   ├── router.py
│   ├── retrieval.py
│   ├── logistics_stub.py
│   └── security.py
│
├── api/
│   └── main.py
│
├── prompts/
│   ├── triage_system_v1.2.0.txt
│   └── pin.json
│
├── evals/
│   ├── golden.jsonl
│   └── run_eval.py
│
├── fixtures/
│   ├── README.md
│   ├── knowledge_base.json
│   └── triage_messages_sample.jsonl
│
├── scripts/
│   ├── build_prompt_pin.py
│   ├── check_prompt_pin.py
│   ├── generate_fixtures.py
│   ├── make_demo_token.py
│   ├── measure_perf.py
│   └── run_demo.py
│
├── evidence/
│   └── demo_transcript.txt
│
├── docs/
│   ├── architecture.md
│   ├── deployment.md
│   ├── cost_analysis.md
│   ├── user_guide.md
│   ├── build_checkpoint.md
│   ├── incident_note.md
│   ├── peer_review_checklist.md
│   ├── presentation_outline.md
│   └── presentation.pdf
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── perf/
│   └── test_security_smoke.py
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Dataset

Primary teaching fixture:

`fixtures/triage_messages_sample.jsonl`

Current size:

```text
300 synthetic rows
```

Generate it with:

```bash
python scripts/generate_fixtures.py
```

The fixture:

- contains synthetic teaching messages
- contains no production patient records
- is not scraped from a live system
- does not contain SokoniHub marketplace fixtures

See:

`fixtures/README.md`

---

## Quick Start

Create and activate a virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run default tests:

```bash
pytest -q
```

Current verified result:

```text
31 passed
```

---

## Minimum Working Product

Run:

```bash
python scripts/run_demo.py
```

A successful demonstration ends with:

```text
MINIMUM WORKING PRODUCT: PASSED
```

Current verified result:

```text
PASSED
Exit code = 0
```

Demo evidence is written to:

`evidence/demo_transcript.txt`

The MWP demonstrates:

1. prompt/version pin
2. 300 synthetic fixtures
3. FastAPI health behavior
4. JWT authentication
5. clinical routing
6. local RAG-style retrieval
7. logistics `check_stock` tool
8. emergency escalation
9. security redaction
10. golden-set evaluation

---

## API

FastAPI application:

`api/main.py`

### Health

Endpoint:

```text
GET /health
```

Manual HTTP verification has returned:

```text
200 OK
```

The response includes:

- service name
- stub mode
- prompt version
- prompt SHA-256

### Triage

Endpoint:

```text
POST /triage
```

Requires JWT authentication.

Supported paths include:

- emergency
- clinical
- logistics

---

## Authentication

JWT authentication is implemented using:

`python-jose`

The API expects:

- `sub`
- `role`

Roles used by the teaching implementation include:

- `clinical_ops`
- `dispatcher`
- `platform_admin`

The signing secret comes from:

`JWT_SECRET`

No real signing secret is committed to Git.

---

## Retrieval

Implementation:

`agents/retrieval.py`

The current RAG-style path uses:

- local knowledge fixtures
- tokenization
- token overlap
- deterministic top-result retrieval

It does not claim to be a production vector database or embedding system.

---

## Logistics Tool

Implementation:

`agents/logistics_stub.py`

Current MCP-style tool:

```text
check_stock
```

It reads from deterministic local teaching fixtures.

It does not query a production inventory backend.

---

## Prompt Pin

Prompt:

`prompts/triage_system_v1.2.0.txt`

Pin:

`prompts/pin.json`

Current version:

```text
1.2.0
```

Check the pin:

```bash
python scripts/check_prompt_pin.py
```

Expected:

```text
PROMPT PIN CHECK: PASSED
```

The hash is normalized for LF line endings to avoid Windows/Linux differences.

---

## Golden Evaluation

Golden set:

`evals/golden.jsonl`

Run:

```bash
python evals/run_eval.py
```

Current verified result:

```text
10/10 correct
Score = 1.00
Threshold = 0.90
EVAL: PASSED
```

This evaluates routing behavior on a small labelled teaching set.

It is not a clinical-quality score.

---

## Testing

### Default / Unit

Run:

```bash
pytest -q
```

Current result:

```text
31 passed
```

### Integration

Run:

```bash
pytest -q -m integration
```

Current result:

```text
8 passed
```

### Security

Run:

```bash
pytest -q tests/test_security_smoke.py
```

The security smoke includes a real redaction test.

### Performance

Run:

```bash
pytest -q -m perf
```

Current result:

```text
1 passed
```

---

## Performance Evidence

Generate the measurement:

```bash
python scripts/measure_perf.py
```

Output:

`perf_stub.json`

Measured local stub run:

```text
iterations = 1000
mean_ms = 0.001053
median_ms = 0.001000
p95_ms = 0.001100
max_ms = 0.006500
network_calls = 0
model_calls = 0
```

These values measure only the local deterministic router on one machine.

They are not production API latency claims.

---

## Security

Security implementation:

`agents/security.py`

Security evidence:

`tests/test_security_smoke.py`

Current controls include:

- JWT authentication
- role restrictions
- Bearer-token redaction
- numeric-identifier redaction
- `.env` exclusion
- no committed production keys
- synthetic fixtures

The project does not claim these controls constitute complete production security.

---

## CI

GitHub Actions workflow:

`.github/workflows/ci.yml`

The workflow runs:

- prompt-pin check
- default tests
- security smoke
- golden evaluation
- integration tests
- stub performance measurement
- performance tests

The golden eval score is printed in CI logs.

---

## Documentation

Required documentation pack:

- [Architecture](docs/architecture.md)
- [Deployment](docs/deployment.md)
- [Cost Analysis](docs/cost_analysis.md)
- [User Guide](docs/user_guide.md)
- [Build Checkpoint](docs/build_checkpoint.md)

Additional evidence:

- [Fixture Documentation](fixtures/README.md)
- [Incident Note](docs/incident_note.md)
- [Demo Guide](DEMO.md)
- [Peer Review Checklist](docs/peer_review_checklist.md)

---

## Build Checkpoint

Current verified technical status:

```text
31 default tests passed
8 integration tests passed
1 performance test passed
10/10 golden eval
300 synthetic fixtures
MWP PASSED
exit code 0
```

See:

`docs/build_checkpoint.md`

for a full distinction between completed and deferred work.

---

## Peer Review

Checklist:

`docs/peer_review_checklist.md`

Review log:

`review_log.md`

A real reviewer name, PR reference, findings and outcome should be recorded before final submission.

If the solo-cohort fallback is used, the self-review should be explicitly identified as such.

---

## Demo

Primary demo command:

```bash
python scripts/run_demo.py
```

See:

`DEMO.md`

A successful run generates:

`evidence/demo_transcript.txt`

---

## Presentation

Outline:

`docs/presentation_outline.md`

Final presentation:

`docs/presentation.pdf`

The presentation should contain 8–10 slides and support the Week 12 demo.

---

## Fallbacks Declared

- [x] No live OpenAI key required for automated tests.
- [x] Deterministic router used in stub mode.
- [x] Local retrieval twin used instead of production vector infrastructure.
- [x] Local logistics stub used instead of production MCP/inventory backend.
- [x] No Docker required for the current local MWP.
- [x] No live cloud deployment claimed.
- [x] No production patient scrape.
- [x] No SokoniHub retail fixtures mixed with clinical fixtures.
- [x] Performance evidence labelled as local stub evidence.
- [x] Golden eval labelled as teaching routing evaluation.

---

## What We Will Not Claim

This capstone does not claim:

- production clinical readiness
- autonomous diagnosis
- regulatory approval
- production-scale RAG
- a live production MCP server
- a live cloud deployment
- production traffic performance
- complete enterprise security

The project demonstrates engineering integration and evidence in a controlled teaching environment.

---

## Submission Checklist

- [x] `proposal.md`
- [x] `skill_matrix.md`
- [x] `integration_map.json`
- [x] synthetic fixtures
- [x] fixture README
- [x] default tests
- [x] integration tests
- [x] performance test
- [x] real security-redaction test
- [x] prompt pin
- [x] golden eval
- [x] one-command demo
- [x] demo transcript
- [x] measured `perf_stub.json`
- [x] CI workflow
- [x] five-document pack
- [x] build checkpoint
- [x] peer-review checklist
- [ ] actual peer-review outcome recorded
- [ ] presentation PDF completed
- [ ] GitHub CI verified green
- [ ] final secret scan completed