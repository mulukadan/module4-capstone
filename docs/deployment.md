# AfyaPlus Module 4 Capstone Deployment Guide

## Deployment Status

The current capstone has been executed locally.

A production cloud deployment has not been performed.

The cloud steps in this document are therefore a deployment plan, not evidence of a live production environment.

---

## Local Requirements

Recommended environment:

- Python 3.12
- virtual environment
- Windows, Linux, or macOS
- internet access only for initial dependency installation

The deterministic MWP does not require:

- OpenAI API access
- GPU
- Docker
- cloud credentials

---

## Local Setup

Clone or open the repository.

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

For a manually started authenticated API, configure:

```text
JWT_SECRET
```

Example for a local PowerShell session:

```powershell
$env:JWT_SECRET="local-development-value"
```

This value must not be committed.

`.env` files are excluded by `.gitignore`.

The one-command demo does not require the user to set a permanent secret because it creates a temporary runtime secret.

---

## Local Verification

Run default tests:

```bash
pytest -q
```

Run integration tests:

```bash
pytest -q -m integration
```

Run performance tests:

```bash
pytest -q -m perf
```

Run prompt pin verification:

```bash
python scripts/check_prompt_pin.py
```

Run the golden evaluation:

```bash
python evals/run_eval.py
```

Run the complete MWP:

```bash
python scripts/run_demo.py
```

---

## Start the API

With `JWT_SECRET` configured:

```bash
uvicorn api.main:app --host 127.0.0.1 --port 8000
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

Expected status:

```text
200 OK
```

---

## CI Deployment Gate

GitHub Actions workflow:

`.github/workflows/ci.yml`

The workflow checks:

- prompt pin
- default tests
- security smoke
- golden evaluation
- integration tests
- performance tests

A deployment should not proceed if these required checks fail.

---

## Container Deployment

A production Docker deployment is not required for this capstone.

If Docker is added later, the deployment should:

1. build from a pinned Python base image
2. install `requirements.txt`
3. copy application code
4. inject secrets at runtime
5. run automated tests before release
6. expose the FastAPI service through a secure HTTPS reverse proxy

No Docker deployment is claimed as executed in the current project.

---

## Cloud Deployment Plan

A future cloud deployment could use:

- Azure App Service
- AWS ECS / App Runner
- Google Cloud Run
- another approved container or application platform

The expected deployment flow would be:

```text
Git push
   ↓
CI tests
   ↓
security and eval gates
   ↓
build artifact
   ↓
staging deployment
   ↓
health check
   ↓
human approval
   ↓
production deployment
```

These cloud steps have not been executed live.

---

## Production Secrets

Production secrets should be stored in a managed secret service such as:

- Azure Key Vault
- AWS Secrets Manager
- Google Secret Manager

Secrets must not be:

- hard-coded
- committed to Git
- printed in logs
- stored in demo evidence

---

## HTTPS

Local HTTP is acceptable for the teaching environment.

A production deployment must use HTTPS.

TLS termination should occur at the approved hosting or reverse-proxy layer.

---

## Rollback

A production release should support rollback to the previous known-good version.

Rollback should restore:

- application version
- prompt pin
- compatible configuration
- required dependencies

The prompt SHA and version should be checked after rollback.

---

## Health Verification

After deployment, verify:

```text
GET /health
```

The endpoint should report:

- `status = ok`
- expected service name
- expected prompt version
- expected prompt SHA

If the prompt pin is unexpected, the deployment should not be treated as verified.

---

## Production Readiness Gaps

Before production use, the project would still need:

- approved clinical governance
- production-grade authentication
- managed secret storage
- persistent audit logging
- monitoring and alerting
- production RAG infrastructure
- robust model evaluation
- production incident response
- data-retention controls
- formal privacy and security review

The current capstone is a teaching implementation and does not claim these items are complete.