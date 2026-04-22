def log_interaction(data):
    return {"status": "Interaction logged", "data": data}


def edit_interaction(data):
    return {"status": "Interaction updated", "data": data}


def get_hcp_details(name):
    return {"doctor": name, "history": ["Visited last week"]}


def suggest_followup(data):
    return {"suggestion": "Follow up in 3 days"}


def summarize_interaction(text):
    return {"summary": text[:50]}