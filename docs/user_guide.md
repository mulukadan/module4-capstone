# AfyaPlus Module 4 Capstone User Guide

## Overview

This guide explains how to run, test and demonstrate the AfyaPlus Module 4 Capstone locally.

The default capstone path uses deterministic stubs and does not require a paid model API.

The main components are:

- FastAPI service
- JWT authentication
- deterministic message router
- local RAG-style retrieval
- logistics `check_stock` stub
- prompt/version pinning
- security redaction
- synthetic fixtures
- golden-set evaluation
- performance measurement
- one-command demo

---

## 1. Open the Project

Project root:

```text
D:\Moringa\module4-capstone
```

In PowerShell:

```powershell
cd D:\Moringa\module4-capstone
```

---

## 2. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script for the current process, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

A successful activation shows:

```text
(.venv)
```

at the start of the prompt.

---

## 3. Install Dependencies

If dependencies are not yet installed:

```powershell
pip install -r requirements.txt
```

---

## 4. Run the Minimum Working Product

The easiest way to demonstrate the capstone is:

```powershell
python scripts/run_demo.py
```

A successful run ends with:

```text
MINIMUM WORKING PRODUCT: PASSED
```

The demo exercises:

- prompt pin verification
- synthetic fixture count
- FastAPI health endpoint
- JWT authentication
- clinical route
- local retrieval
- logistics `check_stock`
- emergency escalation
- security redaction
- golden-set evaluation

The demo also creates:

```text
evidence/demo_transcript.txt
```

---

## 5. Run Default Tests

Run:

```powershell
pytest -q
```

Current successful result:

```text
31 passed
```

These are the default tests configured through:

```text
pytest.ini
```

Integration and performance markers are excluded from the default run.

---

## 6. Run Integration Tests

Run:

```powershell
pytest -q -m integration
```

Current successful result:

```text
8 passed
```

These tests exercise FastAPI application boundaries using the test client.

---

## 7. Run Performance Tests

Run:

```powershell
pytest -q -m perf
```

Current successful result:

```text
1 passed
```

The performance test measures the local deterministic router.

It is not a production API performance benchmark.

---

## 8. Run the Security Smoke

Run:

```powershell
pytest -q tests/test_security_smoke.py
```

The security smoke verifies:

- Bearer-token redaction
- numeric-identifier redaction
- combined redaction
- removal of raw Bearer tokens
- preservation of safe text

---

## 9. Check the Prompt Pin

Run:

```powershell
python scripts/check_prompt_pin.py
```

Expected final line:

```text
PROMPT PIN CHECK: PASSED
```

The expected and actual SHA-256 values should match.

---

## 10. Run the Golden Evaluation

Run:

```powershell
python evals/run_eval.py
```

Current successful result:

```text
Score: 10/10 = 1.00
Threshold: 0.90
EVAL: PASSED
```

The golden set measures routing behavior on a small labelled teaching set.

It is not a clinical-accuracy benchmark.

---

## 11. Generate Synthetic Fixtures

Run:

```powershell
python scripts/generate_fixtures.py
```

Expected:

```text
Generated 300 synthetic triage rows.
```

Verify row count:

```powershell
(Get-Content .\fixtures\triage_messages_sample.jsonl).Count
```

Expected:

```text
300
```

---

## 12. Measure Stub Performance

Run:

```powershell
python scripts/measure_perf.py
```

The output is written to:

```text
perf_stub.json
```

The result records:

- iterations
- mean latency
- median latency
- p95 latency
- maximum latency
- network calls
- model calls

The measurement is explicitly local and stub-only.

---

## 13. Start the FastAPI Service Manually

Set a local JWT secret for the current PowerShell session:

```powershell
$env:JWT_SECRET="local-development-value"
```

Start the service:

```powershell
uvicorn api.main:app --host 127.0.0.1 --port 8000
```

The service should start on:

```text
http://127.0.0.1:8000
```

---

## 14. Check the Health Endpoint

From another terminal:

```powershell
curl.exe http://127.0.0.1:8000/health
```

Expected fields include:

- `status`
- `service`
- `mode`
- `prompt_version`
- `prompt_sha256`

Example:

```json
{
  "status": "ok",
  "service": "afyaplus-module4-capstone",
  "mode": "stub",
  "prompt_version": "1.2.0"
}
```

---

## 15. Generate a Demo JWT

For a clinical user:

```powershell
$env:JWT_SECRET="local-development-value"
$TOKEN = python scripts/make_demo_token.py clinical_ops
```

For a dispatcher:

```powershell
$TOKEN = python scripts/make_demo_token.py dispatcher
```

The token is generated locally.

Do not commit JWTs or signing secrets.

---

## 16. Test Clinical Triage Manually

Using PowerShell:

```powershell
$BODY = @{
    message = "I have fever for two days"
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/triage" `
  -Method POST `
  -Headers @{
      Authorization = "Bearer $TOKEN"
  } `
  -ContentType "application/json" `
  -Body $BODY
```

Expected route:

```text
clinical
```

The response should include a retrieved knowledge record.

---

## 17. Test Logistics Manually

Create a dispatcher token:

```powershell
$TOKEN = python scripts/make_demo_token.py dispatcher
```

Then:

```powershell
$BODY = @{
    message = "Do we have amoxicillin in stock?"
    clinic = "Central Clinic"
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/triage" `
  -Method POST `
  -Headers @{
      Authorization = "Bearer $TOKEN"
  } `
  -ContentType "application/json" `
  -Body $BODY
```

Expected tool:

```text
check_stock
```

Expected teaching quantity for Central Clinic amoxicillin:

```text
40
```

---

## 18. Stub Path

The default capstone uses the stub path.

That means:

- router is deterministic
- retrieval is local
- logistics data is local
- tests make no paid model calls
- performance tests make no network calls
- demo does not require OpenAI access

This is intentional so CI remains cheap and reproducible.

---

## 19. Known Dependency Warning

Some test runs may show a Starlette deprecation warning related to `httpx` and `TestClient`.

The warning does not currently cause test failures.

Current tests remain green.

This should be reviewed during future dependency upgrades rather than hidden.

---

## 20. Troubleshooting

### `ModuleNotFoundError`

Run commands from the repository root:

```text
D:\Moringa\module4-capstone
```

Make sure the virtual environment is active.

### JWT authentication fails

Confirm:

```powershell
$env:JWT_SECRET
```

is set in the same environment where the server is running.

### JSON decode error in PowerShell

Prefer:

```powershell
ConvertTo-Json
```

with:

```powershell
Invoke-RestMethod
```

rather than manually escaping JSON strings.

### Prompt pin check fails

Run:

```powershell
python scripts/build_prompt_pin.py
```

only if the prompt was intentionally changed and the new version should be pinned.

Do not regenerate a pin simply to hide an unexpected prompt change.

---

## 21. Evidence Files

Important evidence includes:

```text
evidence/demo_transcript.txt
perf_stub.json
evals/golden.jsonl
fixtures/triage_messages_sample.jsonl
prompts/pin.json
```

These files support the technical claims made in the capstone.

---

## 22. Recommended Demo Sequence

For a short live demonstration:

1. run `python scripts/run_demo.py`
2. show `MINIMUM WORKING PRODUCT: PASSED`
3. show `pytest -q`
4. show the golden eval score
5. briefly show `/health`
6. explain what is stubbed versus what would be productionized later

This keeps the demonstration clear, reproducible and honest.