from AGENTS.evidence_agent import run as evidence
from AGENTS.export_review_agent import run as export_review
from AGENTS.item_scope_agent import run as item_scope
from AGENTS.license_question_agent import run as license_question
from AGENTS.party_destination_agent import run as party_destination
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run export-control specialists and apply fail-closed compliance governance."""
    outputs = {
        "item_scope": item_scope(context),
        "party_destination": party_destination(context),
        "license_question": license_question(context),
        "evidence": evidence(context),
        "review": export_review(context),
    }
    governance = authorize("export_control_support_release", context)
    return {
        "system": "F108",
        **outputs,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_export_control_review_required": True,
        "autonomous_export_authority": False,
        "autonomous_classification_authority": False,
        "autonomous_license_authority": False,
    }
