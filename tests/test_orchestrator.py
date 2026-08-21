from orchestration.orchestrator import run

def test_human_review_gate():
    result=run({"item":{"name":"example"}})
    assert result["review"]["decision"]=="human_review_required"
