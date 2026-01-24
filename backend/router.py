def route_condition(state) -> str:
    msg = state["message"].lower()

    if any(x in msg for x in [
        "company", "fly your tech", "fyt", "services",
        "what do you do", "contact", "email", "phone",
        "technology", "tech stack", "about"
    ]):
        return "company"

    if any(x in msg for x in ["lead", "customer", "client"]):
        return "lead"

    if any(x in msg for x in ["schedule", "meeting", "appointment"]):
        return "schedule"

    return "llm"
