# F108 | Agentic Export Control | L3 Gold Standard | v1.0

A governed multi-agent reference system for export-control review support, including item scoping, jurisdiction and classification review, party and destination screening, end-use and end-user review, license-question triage, evidence organization, and qualified human compliance review.

## Five-agent architecture

- Item Scope Agent
- Party and Destination Agent
- License Question Agent
- Evidence Agent
- Export Review Agent

## Gold-standard export-control governance

F108 is fail closed and compliance-support only. Release requires reviewed item scope, jurisdiction, classification, parties and destination, end use and end user, license questions, evidence provenance, and explicit qualified export-control approval.

Release is blocked for unresolved jurisdiction or classification questions, restricted-party matches, prohibited-destination or end-use risks, uncertain license requirements or exception eligibility, deemed-export risk, recordkeeping gaps, missing evidence provenance, or unsupported compliance conclusions.

The reference system cannot autonomously authorize exports, issue final classifications, make license determinations, clear restricted parties, approve technology releases, or submit externally. Final determinations remain with authorized export-control personnel and qualified legal or compliance professionals.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out export-control suite.
