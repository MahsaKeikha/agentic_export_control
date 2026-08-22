from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
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


def test_complete_review_can_release_support_package():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_export_authority"] is False


def test_missing_qualified_review_fails_closed():
    context = valid_context()
    context["qualified_export_control_approval"] = False
    assert run(context)["release_allowed"] is False


def test_export_authorization_is_never_autonomous():
    assert authorize("authorize_export", valid_context())["allowed"] is False


def test_restricted_party_match_blocks_release():
    context = valid_context()
    context["restricted_party_match"] = True
    assert run(context)["release_allowed"] is False


def test_prohibited_end_use_blocks_release():
    context = valid_context()
    context["prohibited_end_use_risk"] = True
    assert run(context)["release_allowed"] is False


def test_license_uncertainty_blocks_release():
    context = valid_context()
    context["license_requirement_uncertain"] = True
    assert run(context)["release_allowed"] is False


def test_deemed_export_risk_blocks_release():
    context = valid_context()
    context["deemed_export_risk"] = True
    assert run(context)["release_allowed"] is False


def test_missing_evidence_provenance_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert run(context)["release_allowed"] is False
