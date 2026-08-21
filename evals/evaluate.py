def evaluate(result):
    return {"has_human_gate": result.get("review",{}).get("decision")=="human_review_required"}
