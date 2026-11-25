# AfyaPlus Teaching Fixtures

## Purpose

This folder contains synthetic teaching fixtures for the Module 4 AfyaPlus capstone.

The primary fixture is:

`triage_messages_sample.jsonl`

It contains approximately 300 synthetic triage-message rows.

## Data source

The rows are generated locally from teaching templates.

They are not scraped from a production system.

They do not contain real patient records.

They do not contain production personally identifiable information.

## Scope

The fixture contains example messages for:

- clinical routing
- emergency routing
- logistics routing

Each record includes:

- fixture ID
- synthetic message
- expected route
- `synthetic: true`

## No-scrape rule

No production health database, marketplace, patient portal, or live website was scraped to create this fixture.

## Domain separation

SokoniHub marketplace fixtures from Week 10 are not mixed with AfyaPlus clinical fixtures.

The two domains remain separate.

## Scale

Current teaching slice:

approximately 300 rows.

This is intentionally within the capstone teaching range rather than a production-scale dataset.