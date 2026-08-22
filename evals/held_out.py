from orchestration.orchestrator import run


def base():
    return {
        "item_scope_reviewed": True,
        "jurisdiction_reviewed": True,
        "classification_reviewed": True,
        "party_destination_reviewed": True,
        "end_use_end_user_reviewed": True,
        "license_question_reviewed": True,
        "evidence_provenance_reviewed": True,
        "qualified_export_control_approval": True,
    }


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "qualified_export_control_approval": False}, False),
    ({**base(), "jurisdiction_uncertain": True}, False),
    ({**base(), "classification_uncertain": True}, False),
    ({**base(), "restricted_party_match": True}, False),
    ({**base(), "prohibited_destination_risk": True}, False),
    ({**base(), "prohibited_end_use_risk": True}, False),
    ({**base(), "license_requirement_uncertain": True}, False),
    ({**base(), "recordkeeping_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
