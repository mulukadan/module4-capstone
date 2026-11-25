# AfyaPlus Capstone Demo

## Minimum Working Product

From the repository root with the virtual environment active, run:

```bash
python scripts/run_demo.py
```

A successful run ends with:

```text
MINIMUM WORKING PRODUCT: PASSED
```

The script demonstrates:

- prompt/version pin verification
- 300-row synthetic fixture evidence
- FastAPI health route
- JWT authentication
- clinical routing
- local RAG-style retrieval
- logistics `check_stock` tool
- emergency escalation
- security redaction
- golden-set evaluation

The demonstration uses deterministic local stubs and does not require a paid model API.

## Evidence

A successful run writes:

`evidence/demo_transcript.txt`

No JWT, secret key, production patient data, or live PII is written to the transcript.