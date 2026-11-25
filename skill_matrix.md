# AfyaPlus Module 4 Skill Matrix

This matrix maps the Module 4 capstone skills to the weeks where they were learned and the final repository artefacts that demonstrate them.

| Skill | Week source | Final capstone evidence | Status |
|---|---|---|---|
| LLM fundamentals | Week 1 | deterministic AI/stub path and architecture documentation | Required |
| Prompt design | Week 2 | `prompts/` and prompt/version pin | Required |
| Retrieval / RAG concepts | Weeks 3–5 | local retrieval path in Minimum Working Product | Required |
| Multimodal concepts | Week 5 / Week 10 | transfer note and provenance practices | Optional transfer |
| FastAPI service | Week 6 | `api/` service and `/health`, `/triage` | Required |
| Authentication | Week 6 | authenticated triage route | Required |
| Logistics MCP | Week 7 | logistics tool used in stub-mode MWP | Required |
| Cost analysis | Week 7 | `docs/cost_analysis.md` | Required |
| Performance measurement | Week 7 / Week 11 | `scripts/measure_perf.py`, `perf_stub.json` | Required |
| Prompt version pinning | Week 8 | prompt pin and pin-field tests | Required |
| Golden-set evaluation | Week 8 | `evals/golden.jsonl`, evaluation score | Required |
| CI/CD | Week 8 | `.github/workflows/ci.yml` | Required |
| Secret hygiene | Week 9 | security smoke tests and README fallback notes | Required |
| RBAC / access control | Week 9 | adapted security controls | Required |
| Redaction | Week 9 | `tests/test_security_smoke.py` real redaction test | Required |
| Security/compliance documentation | Week 9 | architecture/deployment/build checkpoint documentation | Required |
| Multimodal honesty/provenance | Week 10 | transfer note; no mixed catalog fixtures | Optional transfer |
| Testing pyramid | Week 11 | unit, integration and perf marker structure | Required |
| Git workflow | Week 11 | feature branches and review log | Required |
| Peer review | Week 11 | `docs/peer_review_checklist.md`, `review_log.md` | Required |
| Presentation | Week 11/12 | `docs/presentation.pdf` | Required |

## Notes

- AfyaPlus clinical fixtures remain separate from Week 10 SokoniHub catalog fixtures.
- Automated tests use deterministic stubs.
- Live OpenAI access is optional for the demo and is not required for CI.
- Cloud deployment is documentation-only unless explicitly executed and evidenced.