# AfyaPlus Module 4 Capstone Proposal

## Project Path

This project uses the recommended AfyaPlus Module 4 Capstone path.

The final system integrates selected work from Weeks 1 to 10 into one health-operations application.

The project combines:

- a triage API
- deterministic routing and stub AI behavior for tests
- logistics MCP tools
- prompt and version pins
- golden-set evaluation
- security and redaction controls
- cost and performance evidence
- documentation and review evidence

The project is designed as a teaching system and does not use production patient data.

---

## Problem

AfyaPlus needs a repeatable and testable way to support health operations without depending on fragile manual processes or uncontrolled AI outputs.

The system should support:

1. authenticated triage requests
2. safe triage routing
3. retrieval of relevant support information
4. one logistics MCP tool path
5. prompt/version pinning
6. security controls
7. regression evaluation
8. measurable cost and performance evidence
9. clear documentation for technical and non-technical reviewers

The system must remain safe to test locally and in CI.

---

## Dataset

The capstone uses synthetic teaching fixtures only.

Target fixture size:

approximately 300 synthetic triage-message rows.

The fixture will be stored under:

`fixtures/`

The dataset will not contain real patient records or production PII.

The capstone will not scrape production systems.

SokoniHub retail catalog fixtures from Week 10 will not be mixed with AfyaPlus clinical fixtures.

---

## Reuse from Previous Weeks

### Weeks 1 to 5

Concepts reused where applicable:

- LLM fundamentals
- prompting
- retrieval-augmented generation concepts
- embeddings and retrieval concepts
- multimodal design principles

### Week 6

Reuse:

- FastAPI triage service
- authenticated `/triage` behavior
- health endpoint
- triage response schema

### Week 7

Reuse:

- logistics MCP concepts and tools
- cost analysis
- batching and cache lessons
- performance measurement

### Week 8

Reuse:

- prompt pinning
- SHA-256 checks
- golden-set evaluation
- CI/CD gating
- version alignment

### Week 9

Reuse:

- transit/security hygiene
- secret handling
- RBAC ideas
- input security
- redaction and audit concepts

### Week 10

Reuse:

- provenance and honesty practices
- separation of fixture domains
- multimodal transfer lessons

Week 10 retail fixtures are not copied into the clinical fixture set.

---

## Minimum Working Product

The Minimum Working Product will demonstrate:

1. authentication
2. deterministic triage routing in stub mode
3. retrieval of relevant local knowledge
4. one logistics MCP tool call
5. prompt/version pin evidence
6. security/redaction smoke test
7. golden-set evaluation score
8. synthetic fixture processing
9. a documented end-to-end demo command

Automated tests will use stubs and will not require paid API access.

---

## Milestones

### Milestone 1

Create project brief, skill matrix and integration map.

### Milestone 2

Build the testing pyramid and security smoke tests.

### Milestone 3

Create the Minimum Working Product and one-command demo.

### Milestone 4

Complete documentation, measured performance and cost evidence.

### Milestone 5

Complete Git workflow and peer review evidence.

### Milestone 6

Prepare the Week 12 presentation and live demo.

---

## Out of Scope

The following are explicitly out of scope for this teaching capstone:

- production patient data
- production hospital deployment
- live cloud infrastructure
- large-scale model retraining
- millions of rows
- automated diagnosis
- fully autonomous clinical decision-making
- production marketplace scraping
- mixing SokoniHub retail fixtures with AfyaPlus health fixtures

The system is designed to assist and demonstrate engineering controls, not replace qualified healthcare professionals.