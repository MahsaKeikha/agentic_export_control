def authorize(action, human_approved=False):
    consequential={"authorize_export","final_classification","license_determination","external_submission"}
    return human_approved if action in consequential else True
