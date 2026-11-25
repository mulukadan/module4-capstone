# AfyaPlus Module 4 Capstone Peer Review Checklist

## Purpose

This checklist is used to review the final capstone before merge and submission.

The reviewer should verify repository evidence rather than relying only on the written project summary.

## Review Checklist

- [ ] `proposal.md` clearly states the project path, problem, dataset scale, milestones and out-of-scope items.
- [ ] `skill_matrix.md` maps Weeks 1 to 10 to final capstone artefacts.
- [ ] `integration_map.json` points to real repository paths and required artefacts exist.
- [ ] `pytest -q` passes.
- [ ] `pytest -q -m integration` passes.
- [ ] `pytest -q -m perf` passes.
- [ ] `tests/test_security_smoke.py` includes a real redaction test.
- [ ] `python scripts/check_prompt_pin.py` passes.
- [ ] `python evals/run_eval.py` meets the configured threshold.
- [ ] `python scripts/run_demo.py` ends with `MINIMUM WORKING PRODUCT: PASSED`.
- [ ] `fixtures/triage_messages_sample.jsonl` contains only synthetic teaching data.
- [ ] SokoniHub marketplace fixtures are not mixed with AfyaPlus clinical fixtures.
- [ ] `perf_stub.json` is clearly labelled as local stub performance.
- [ ] `.env`, JWT secrets and API keys are not committed.
- [ ] The five required documentation files exist.
- [ ] `docs/build_checkpoint.md` separates working and deferred items.
- [ ] The README does not overclaim live cloud, live LLM, production RAG or production MCP.
- [ ] `evidence/demo_transcript.txt` contains no secrets or real patient information.
- [ ] `docs/presentation.pdf` matches the actual tested implementation.
- [ ] Review findings and outcome are recorded in `review_log.md`.

## Reviewer Outcome

Record one of:

- Approved
- Approved with minor follow-up
- Changes requested