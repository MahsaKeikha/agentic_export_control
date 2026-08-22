from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "item": {"name": "example"},
    "parties": [],
    "destination": "example",
    "item_scope_reviewed": True,
    "jurisdiction_reviewed": True,
    "classification_reviewed": True,
    "party_destination_reviewed": True,
    "end_use_end_user_reviewed": True,
    "license_question_reviewed": True,
    "evidence_provenance_reviewed": True,
    "qualified_export_control_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
