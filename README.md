# F108 | Agentic Export Control | L3 Gold Standard | v1.0

A governed five-agent reference architecture for export-control workflow support across item scoping, jurisdiction review, classification research, party and destination screening, end-use and end-user analysis, license-question triage, technology-release risk, evidence provenance, recordkeeping, and qualified human export-control approval.

F108 is compliance-support only. It organizes facts, evidence, risks, and review workflows without exercising binding export authorization, final classification, licensing, restricted-party clearance, technology-release approval, legal advice, or external-submission authority.

## Export-control lifecycle

```text
Item / Technology Intake
        -> Jurisdiction Review
        -> Classification Review
        -> Party and Destination Screening
        -> End-Use and End-User Review
        -> License Question Triage
        -> Evidence and Recordkeeping Review
        -> Qualified Human Export-Control Approval
```

The workflow fails closed when material jurisdiction, classification, party, destination, end-use, license, evidence, or recordkeeping questions remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Item Scope Agent | Structures the item, software, technology, technical data, source, destination, purpose, and known jurisdictional facts | What exactly is being exported, transferred, released, or accessed? |
| Party and Destination Agent | Organizes parties, locations, destinations, screening evidence, and transaction roles | Who is involved, where are they located, and what screening or destination risks require review? |
| License Question Agent | Frames licensing, exception, exemption, end-use, end-user, and authorization questions for qualified review | What licensing or authorization questions remain unresolved? |
| Evidence Agent | Preserves source provenance, classification support, screening evidence, dates, and recordkeeping state | What evidence supports the export-control analysis? |
| Export Review Agent | Performs independent readiness review before a support package can be released | Have all required reviews and qualified-human approvals been completed? |

No agent independently authorizes an export, issues a binding classification, clears a restricted party, approves a technology release, or makes a final license determination.

## Repository structure

```text
AGENTS/
├── item_scope_agent.py
├── party_destination_agent.py
├── license_question_agent.py
├── evidence_agent.py
└── export_review_agent.py

SKILLS/
├── item_scoping.py
├── party_screening_workflow.py
├── license_question_triage.py
├── evidence_discipline.py
└── human_approval.py

TOOLS/
├── item_register.py
├── party_register.py
├── destination_matrix.py
├── evidence_tracker.py
└── risk_matrix.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates multi-agent reasoning from deterministic registers, screening support, evidence tracking, risk scoring, safety policy, evaluation, memory, and observability.

## Item scoping

`SKILLS/item_scoping.py` and `TOOLS/item_register.py` support structured intake of physical goods, software, technology, technical data, source code, documentation, or other potentially controlled subject matter.

A governed item record can include:

```text
item_id
item_name
model_or_version
technical_description
function
performance_characteristics
materials_or_components
software_features
encryption_features
source_code_involved
technology_or_technical_data
country_of_origin
manufacturer
owner
current_location
proposed_destination
transfer_method
intended_use
known_end_user
classification_candidates
jurisdiction_candidates
evidence_references
```

Missing technical facts should remain unresolved rather than being inferred from marketing descriptions or product names.

## Export-control jurisdiction

Before classification or licensing analysis, the workflow should identify the potentially applicable export-control jurisdiction or regimes.

Jurisdiction review can consider:

- item origin
- current location
- content or components
- software or technology origin
- prior incorporation of controlled content
- destination
- parties
- transaction structure
- organizational status
- applicable government authority

`jurisdiction_uncertain` is an explicit fail-closed blocker.

F108 must not assume that every item is governed by the same regime, or that an item is uncontrolled merely because it is commercial, publicly marketed, or widely available.

## Classification review

Classification can involve goods, software, technology, technical data, encryption, or other regulated subject matter.

The workflow should preserve:

```text
candidate classification
supporting technical facts
source authority
source date
competing interpretation
reviewer
confidence
open question
```

`classification_uncertain` blocks release when item, software, or technology classification remains unresolved.

## Final-classification boundary

`final_classification` is a protected action.

F108 can organize classification research and evidence but cannot autonomously issue a binding export-control classification. Final classification remains with qualified export-control personnel, counsel, authorized organizational officials, or competent government authorities as applicable.

## Party screening

`SKILLS/party_screening_workflow.py` and `TOOLS/party_register.py` support structured screening workflows.

Party records can include:

- legal name
- aliases
- address
- country
- role
- ownership information
- affiliations
- screening source
- screening date
- screening result
- match rationale
- reviewer
- resolution status

A potential match is not automatically a confirmed prohibited party. Conversely, an unresolved potential match must not be silently cleared.

`restricted_party_match` blocks release and requires qualified review.

## Restricted-party clearance boundary

`restricted_party_clearance` is protected.

The reference system may organize screening evidence and possible matches, but it cannot issue a binding legal clearance for a person, organization, vessel, intermediary, customer, supplier, or other party.

## Destination review

`TOOLS/destination_matrix.py` supports structured review of destination-related risk.

Destination analysis can consider:

- destination country
- transshipment points
- end-user location
- access location
- embargoes or restrictions
- licensing sensitivity
- organization-specific controls

`prohibited_destination_risk` blocks release when a destination restriction or embargo concern remains unresolved.

## End-use and end-user review

Export-control analysis often depends on more than the item and destination.

Review can consider:

- stated end use
- actual end user
- military or government involvement
- nuclear, missile, chemical, biological, or other proliferation-sensitive activity
- surveillance or security use
- diversion indicators
- unusual transaction structure
- inconsistent customer statements
- known intermediaries

`prohibited_end_use_risk` blocks release when end-use or end-user restrictions remain unresolved.

## License-question triage

`SKILLS/license_question_triage.py` supports structured identification of licensing questions without converting them into autonomous legal determinations.

Questions can include:

- whether a license may be required
- whether an exception or exemption might apply
- whether prior authorization exists
- whether conditions or limitations apply
- whether reexport or retransfer restrictions exist
- whether access controls are required
- whether a government filing or application is needed

`license_requirement_uncertain` is an explicit blocker.

## License-determination boundary

`license_determination` is protected.

F108 cannot autonomously decide that a license is required, not required, available, approved, or unnecessary. It also cannot claim that an exception or exemption applies without qualified review.

## Deemed-export and technology-release risk

Export controls may apply to access to technology, technical data, source code, or controlled know-how even without a physical shipment.

Potential contexts can include:

- employee or contractor access
- remote access
- cloud systems
- collaborative research
- source-code repositories
- technical support
- demonstrations
- shared laboratories
- foreign-person access

`deemed_export_risk` blocks release when technology-release or deemed-export concerns remain unresolved.

## Technology-release approval boundary

`technology_release_approval` is protected.

The system cannot approve access to controlled technology, software, source code, technical data, or other restricted information.

## Software and source code

Software can create distinct export-control questions involving functionality, encryption, source code, object code, distribution method, cloud access, technical support, and updates.

The workflow should capture version and configuration rather than assume one classification applies to all releases of a software product.

## Encryption considerations

Where encryption is relevant, review can consider:

- cryptographic functionality
- key-management features
- intended users
- distribution model
- source-code availability
- product category
- technical parameters

F108 should not infer encryption classification solely from the presence or absence of common security features.

## Research and academic contexts

Research environments can involve publications, prototypes, controlled technical information, foreign-person access, sponsored work, laboratory equipment, and international collaboration.

The system can organize questions around publication status, access restrictions, sponsor terms, technology scope, and participants. It cannot autonomously declare research exempt or outside export-control jurisdiction.

## Publicly available and published information boundaries

Some regimes may treat published or publicly available information differently from controlled technical information, but these distinctions are jurisdiction-specific and fact-dependent.

F108 should not infer an exclusion merely because information appears online, has been presented publicly, or is intended for publication.

## Fundamental-research boundary

Where a fundamental-research concept exists, applicability may depend on the institution, jurisdiction, contractual restrictions, publication controls, access restrictions, and subject matter.

The system can identify the question and supporting facts but cannot make a binding legal determination.

## Destination, nationality, and access distinctions

Physical destination, user nationality, citizenship, residency, employer, and actual access location can have different legal significance depending on the governing regime.

The system should avoid collapsing these facts into a single country field when they materially differ.

## Reexports and retransfers

A transaction can create downstream restrictions after the initial export.

Review can identify:

- reexport destination
- new end user
- new end use
- transfer of controlled technology
- changed ownership or control
- license conditions
- authorization limitations

F108 should preserve downstream restrictions rather than assuming an initial authorization covers future transfers.

## Foreign-produced items and controlled content

Some export-control regimes can apply to foreign-produced items based on controlled content, technology, software, or production rules.

The system can organize relevant technical and sourcing facts, but material jurisdictional uncertainty must be escalated.

## Recordkeeping

`recordkeeping_gap` is an explicit blocker.

A governed export-control record can preserve:

```text
transaction_id
item_scope
classification_evidence
jurisdiction_analysis
party_screening
destination_review
end_use_end_user_review
license_question_state
authorization_references
reviewer
approval
dates
retention_metadata
```

The reference system should not invent retention periods. Organization-specific requirements should come from applicable law, regulation, policy, authorization conditions, or qualified review.

## Evidence provenance

`SKILLS/evidence_discipline.py` and `TOOLS/evidence_tracker.py` support provenance tracking.

Material evidence can include:

- product specifications
- engineering documentation
- supplier classifications
- government rulings or guidance
- screening results
- end-use statements
- customer declarations
- authorization documents
- prior reviews
- internal records

`evidence_provenance_missing` blocks release when classification or screening support cannot be adequately traced.

## Evidence hierarchy and uncertainty

The workflow should distinguish among:

```text
verified technical fact
supplier assertion
customer assertion
government source
internal prior determination
automated inference
unresolved question
qualified-human determination
```

A supplier classification can be useful evidence but should not automatically become the organization's final legal position.

## Unsupported compliance conclusions

`unsupported_compliance_conclusion` blocks release when an export-control conclusion exceeds reviewed evidence or authority.

Examples include unsupported claims that:

- an item is definitively uncontrolled
- a party is legally cleared
- no license is required
- an exception applies
- a destination is permitted
- a technology release is authorized
- a classification is final

The system should express uncertainty and route unresolved questions instead.

## Risk triage

`TOOLS/risk_matrix.py` can support structured prioritization of issues such as:

- jurisdiction uncertainty
- classification uncertainty
- restricted-party matches
- prohibited destinations
- end-use concerns
- end-user concerns
- licensing uncertainty
- deemed-export risk
- technology-access concerns
- recordkeeping gaps
- evidence gaps

Risk scores are review aids, not legal conclusions.

## Organization roles and separation of duties

A governed implementation should preserve role distinctions among:

- engineers and product teams
- sales and business teams
- shipping and logistics
- procurement
- research personnel
- IT and security
- export-control professionals
- compliance
- legal counsel
- authorized corporate officers

The system should not allow a business owner to implicitly substitute for a qualified export-control approver when organizational policy requires independent review.

## Change management

Material changes can invalidate prior analysis.

Examples include:

- product redesign
- software update
- encryption change
- changed destination
- changed end user
- changed end use
- new intermediary
- ownership change
- sanctions-list update
- regulation change
- license expiration
- new technology access

A governed system should trigger re-review when such changes affect the basis of the earlier determination.

## Effective dates and source freshness

Export-control rules, lists, classifications, license exceptions, and embargoes can change.

The workflow should preserve:

- source
- source date
- effective date
- review date
- transaction date
- known superseding authority

A stale screening result or prior classification should not automatically remain valid for a later transaction.

## Privacy and confidentiality

Export-control workflows can contain employee information, citizenship or nationality data where legally relevant, customer information, technical specifications, source code, restricted technology, screening results, and government correspondence.

Implementations should apply data minimization, access control, secure storage, retention limits, and role-based handling appropriate to the sensitivity of the information.

## Required reviews

The implemented policy requires all eight review conditions:

```text
item_scope_reviewed
jurisdiction_reviewed
classification_reviewed
party_destination_reviewed
end_use_end_user_reviewed
license_question_reviewed
evidence_provenance_reviewed
qualified_export_control_approval
```

Missing any required review fails closed.

## Fail-closed governance

The implemented governance blocks release when any of the following remains unresolved:

- export-control jurisdiction uncertainty
- item, software, or technology classification uncertainty
- restricted-party screening match
- prohibited-destination or embargo risk
- prohibited end-use or end-user risk
- license requirement or exception uncertainty
- technology-release or deemed-export risk
- required recordkeeping gap
- screening or classification evidence provenance gap
- unsupported export-control conclusion
- missing required review
- missing qualified export-control approval

The support package can be released only after required reviews are satisfied and blockers are cleared by the appropriate qualified humans.

## Protected actions

The policy permanently protects:

```text
authorize_export
final_classification
license_determination
restricted_party_clearance
technology_release_approval
external_submission
```

Protected actions remain outside autonomous authority even when every review flag is true.

## Export-authorization boundary

`authorize_export` is protected.

F108 cannot authorize shipment, transmission, release, reexport, retransfer, access, download, or other controlled transfer.

## External-submission boundary

`external_submission` is protected.

The system cannot autonomously submit applications, classifications, license requests, filings, certifications, government correspondence, or other binding representations to regulators or external parties.

## Human authority boundaries

F108 must not autonomously:

- authorize an export or reexport
- issue a final classification
- make a final license determination
- clear a restricted-party match
- approve technology access or release
- determine that an exception or exemption applies
- sign an export certification
- submit a license application
- make a binding legal conclusion
- communicate as an authorized government or corporate representative
- submit externally on behalf of an organization

Final authority remains with qualified export-control, compliance, legal, technical, and organizational personnel according to the applicable regime and governance structure.

## End-to-end reference workflow

A typical F108 workflow follows this sequence:

1. Capture the item, software, technology, or technical-data scope.
2. Record technical facts and evidence.
3. Identify the potentially applicable jurisdiction.
4. Review candidate classification and unresolved technical questions.
5. Register and screen parties and destinations.
6. Review end use and end user.
7. Identify licensing, exception, exemption, or authorization questions.
8. Review deemed-export and technology-release risks.
9. Preserve evidence provenance and source dates.
10. Review recordkeeping requirements and documentation completeness.
11. Triage unresolved risks for qualified specialist review.
12. Perform independent export-control readiness review.
13. Apply fail-closed governance gates.
14. Require explicit qualified-human export-control approval.
15. Keep export authorization, final classification, license determinations, restricted-party clearance, technology-release approval, and external submissions outside autonomous authority.

## Explicit failure states

Useful explicit states include:

```text
ITEM SCOPE INCOMPLETE
JURISDICTION UNCERTAIN
CLASSIFICATION UNCERTAIN
RESTRICTED PARTY MATCH
PROHIBITED DESTINATION RISK
PROHIBITED END USE RISK
LICENSE REQUIREMENT UNCERTAIN
DEEMED EXPORT RISK
TECHNOLOGY RELEASE RISK
RECORDKEEPING GAP
EVIDENCE PROVENANCE MISSING
EXPORT CONTROL CONCLUSION UNSUPPORTED
QUALIFIED EXPORT CONTROL APPROVAL REQUIRED
EXPORT AUTHORIZATION PROHIBITED
FINAL CLASSIFICATION PROHIBITED
LICENSE DETERMINATION PROHIBITED
RESTRICTED PARTY CLEARANCE PROHIBITED
TECHNOLOGY RELEASE APPROVAL PROHIBITED
EXTERNAL SUBMISSION PROHIBITED
```

The system should never fabricate classifications, licenses, government determinations, screening results, end-use evidence, authorizations, approvals, or filings.

## Observability

The `observability/` layer supports traceability across the export-control workflow.

Useful telemetry includes:

- item-scope review state
- jurisdiction review state
- classification candidates
- party-screening state
- destination risk
- end-use and end-user review state
- license-question status
- deemed-export flags
- evidence provenance
- recordkeeping status
- unresolved blockers
- qualified approval state
- protected-action attempts

Observability supports accountability but does not create export-control authority.

## Memory and state

The `memory/` layer can preserve structured workflow context across agents.

State should distinguish verified technical facts, source documents, customer or supplier assertions, screening results, automated analysis, reviewer conclusions, and unresolved questions.

Controlled or sensitive technical information should not be retained or exposed beyond operational and legal need.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test both workflow usefulness and governance behavior, including:

- item-scope completeness
- jurisdiction uncertainty detection
- classification uncertainty detection
- restricted-party escalation
- destination-risk enforcement
- end-use and end-user escalation
- licensing-uncertainty enforcement
- deemed-export detection
- recordkeeping enforcement
- evidence provenance
- unsupported-conclusion detection
- qualified-human approval enforcement
- protected-action enforcement

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out export-control suite.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates cover syntax-critical linting, direct governance behavior, held-out scenarios, and execution of the governed reference workflow.

## Reproducibility

Install development dependencies:

```bash
python -m pip install -e .
```

Then run:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

## Extension points

Organization-specific implementations can add governed integrations for:

- product master data
- engineering configuration systems
- export-classification repositories
- restricted-party screening services
- sanctions data
- licensing systems
- HR and identity systems
- research administration systems
- source-code repositories
- document management
- ERP and shipping systems
- trade compliance platforms

Integrations should preserve source provenance, effective dates, role-based access, human authority, and fail-closed behavior.

## Example applications

Potential governed uses include:

- product export-control intake
- classification research support
- restricted-party screening workflow
- destination review
- end-use and end-user analysis
- license-question preparation
- deemed-export review support
- technology-access governance
- research collaboration screening
- export-control training and simulation

F108 is not an export-control authority, sanctions authority, licensing authority, regulator, law firm, or autonomous authorization system.

## Design principles

F108 follows these principles:

1. Scope the item and technology before drawing export-control conclusions.
2. Preserve technical, screening, and regulatory provenance.
3. Keep jurisdiction, classification, party, destination, end-use, and licensing uncertainty explicit.
4. Treat screening results as evidence requiring qualified review, not automatic legal clearance.
5. Include software, technology, source code, and intangible access in export-control scope when relevant.
6. Trigger re-review when product, party, destination, regulation, or access conditions change.
7. Fail closed when evidence or required review is incomplete.
8. Keep authorization, final classification, license determinations, restricted-party clearance, technology-release approval, and external submissions under qualified human authority.

## Scope statement

F108 demonstrates a governed multi-agent architecture for export-control support. It combines specialized agents, deterministic registers and matrices, evidence discipline, risk triage, memory, observability, evaluation, and fail-closed governance while preserving strict boundaries around export authorization, classification, licensing, restricted-party clearance, technology release, and external submission.

It is a reference implementation for governed export-control workflow engineering, not a substitute for qualified professional, legal, organizational, or government judgment.