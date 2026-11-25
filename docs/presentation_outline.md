# AfyaPlus Module 4 Capstone Presentation Outline

## Slide 1 — Problem and User

**Title:** AfyaPlus Module 4 Capstone

Problem:

AfyaPlus needs a testable health-operations workflow that can route requests, retrieve relevant teaching information and support logistics without uncontrolled AI behavior.

Users:

- clinical operations staff
- dispatch/logistics staff
- platform administrators

Key principle:

Human review remains required for clinical and emergency decisions.

---

## Slide 2 — Path Chosen and Why

Chosen path:

AfyaPlus recommended Module 4 capstone.

Why:

- reuses Weeks 1–10
- demonstrates API, RAG, MCP, security, pins and evaluation
- can run deterministically without paid API calls
- allows strong automated evidence

Teaching fixture:

300 synthetic triage-message rows.

---

## Slide 3 — Architecture

Flow:

```text
Client
  ↓
FastAPI
  ↓
JWT Authentication
  ↓
Router
 ┌───────────┼────────────┐
 ↓           ↓            ↓
Emergency  Clinical    Logistics
 ↓           ↓            ↓
Human     Retrieval    check_stock
review    RAG twin     stub tool
```

Supporting controls:

- prompt pin
- redaction
- golden evaluation
- CI
- performance measurement

---

## Slide 4 — Week 1–10 Skill Coverage

Weeks 1–5:

- LLM, prompting and RAG concepts

Week 6:

- FastAPI and authenticated triage

Week 7:

- logistics tools, cost and performance

Week 8:

- pins, eval and CI

Week 9:

- authentication, access control and redaction

Week 10:

- provenance and honest fallback practices

Evidence:

`skill_matrix.md`

---

## Slide 5 — Live Demo

Primary command:

```text
python scripts/run_demo.py
```

The demo proves:

- prompt SHA match
- 300 synthetic fixtures
- health route
- JWT auth
- clinical retrieval
- logistics `check_stock`
- emergency escalation
- redaction
- golden eval

Successful ending:

```text
MINIMUM WORKING PRODUCT: PASSED
```

Backup evidence:

`evidence/demo_transcript.txt`

---

## Slide 6 — Testing Evidence

Default tests:

```text
31 passed
```

Integration:

```text
8 passed
```

Performance:

```text
1 passed
```

Golden eval:

```text
10/10
Score = 1.00
Threshold = 0.90
```

Testing pyramid:

- unit/default
- integration
- performance

---

## Slide 7 — Security and Compliance Choices

Implemented:

- JWT authentication
- role restrictions
- Bearer-token redaction
- identifier redaction
- `.env` excluded from Git
- synthetic fixtures
- no production scrape
- AfyaPlus/SokoniHub fixture separation

Not claimed:

- complete production security
- regulator approval
- production clinical readiness

---

## Slide 8 — Cost and Performance

Default automated path:

```text
Paid model calls = 0
Estimated API cost = $0
```

Performance evidence:

```text
1000 router iterations
p95 = 0.001100 ms
network calls = 0
model calls = 0
```

Important:

This is local deterministic router performance, not production API latency.

Optional live demonstration may use limited paid calls if explicitly enabled.

---

## Slide 9 — What Works vs Deferred

Works:

- FastAPI
- JWT auth
- router
- local retrieval
- logistics stub
- pin verification
- security redaction
- eval
- tests
- MWP
- documentation

Deferred:

- live LLM
- production vector DB
- production MCP server
- cloud deployment
- managed secrets
- formal clinical/legal approval

---

## Slide 10 — Process and Next Steps

Process evidence:

- feature branch
- PR
- peer-review checklist
- review log
- CI workflow
- build checkpoint

Next steps:

1. production-grade RAG evaluation
2. managed secret service
3. cloud staging environment
4. monitoring and audit logging
5. clinical/security/privacy review
6. controlled pilot before production consideration

Closing message:

The capstone demonstrates an evidence-backed AI engineering workflow while being explicit about what is stubbed, measured and deferred.