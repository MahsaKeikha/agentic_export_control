"""Fail-closed compliance governance for F108 Export Control."""

PROTECTED_ACTIONS = {
    "authorize_export",
    "final_classification",
    "license_determination",
    "restricted_party_clearance",
    "technology_release_approval",
    "external_submission",
}

REQUIRED_REVIEWS = (
    "item_scope_reviewed",
    "jurisdiction_reviewed",
    "classification_reviewed",
    "party_destination_reviewed",
    "end_use_end_user_reviewed",
    "license_question_reviewed",
    "evidence_provenance_reviewed",
    "qualified_export_control_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding export-control authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required export-control review", "missing": missing}

    blockers = []
    if context.get("jurisdiction_uncertain"):
        blockers.append("export-control jurisdiction unresolved")
    if context.get("classification_uncertain"):
        blockers.append("item, software, or technology classification unresolved")
    if context.get("restricted_party_match"):
        blockers.append("restricted-party screening match requires qualified review")
    if context.get("prohibited_destination_risk"):
        blockers.append("destination restriction or embargo risk unresolved")
    if context.get("prohibited_end_use_risk"):
        blockers.append("end-use or end-user restriction risk unresolved")
    if context.get("license_requirement_uncertain"):
        blockers.append("license requirement or exception eligibility unresolved")
    if context.get("deemed_export_risk"):
        blockers.append("technology-release or deemed-export risk unresolved")
    if context.get("recordkeeping_gap"):
        blockers.append("required export-control recordkeeping incomplete")
    if context.get("evidence_provenance_missing"):
        blockers.append("screening or classification evidence provenance incomplete")
    if context.get("unsupported_compliance_conclusion"):
        blockers.append("export-control conclusion exceeds reviewed evidence or authority")

    if blockers:
        return {"allowed": False, "reason": "export-control governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "export-control support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
