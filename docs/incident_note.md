# Incident Note: Manual Triage Request JSON Failure

## Date

24 November 2026

## Symptom

A manual request to:

`POST /triage`

returned an HTTP JSON parsing error.

The API response reported that the JSON body could not be decoded.

## Initial command

The request was sent from PowerShell using escaped quotation marks inside a single-quoted JSON string.

This caused literal backslashes to be passed to the API.

## Diagnosis

The FastAPI endpoint and authentication path were working.

The failure occurred before application routing because the request body itself was invalid JSON.

The issue was therefore a test/request fixture formatting problem rather than a triage-service logic failure.

## Fix

The PowerShell request body was corrected to use valid JSON without unnecessary backslash escaping.

A second supported path uses:

`ConvertTo-Json`

with `Invoke-RestMethod`.

## Verification

The `/health` endpoint returned HTTP 200.

Automated integration tests for `/triage` also passed.

Current integration evidence:

`8 passed`

## Lesson

Manual test fixtures and shell quoting should be treated as part of reproducible test evidence.

A failing request should be diagnosed before changing application logic.