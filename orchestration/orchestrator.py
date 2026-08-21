from AGENTS.item_scope_agent import run as item_scope
from AGENTS.party_destination_agent import run as party_destination
from AGENTS.license_question_agent import run as license_question
from AGENTS.evidence_agent import run as evidence
from AGENTS.export_review_agent import run as export_review

def run(context):
    return {"item_scope":item_scope(context),"party_destination":party_destination(context),"license_question":license_question(context),"evidence":evidence(context),"review":export_review(context)}
