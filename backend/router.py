def route_condition(state) -> str:
    msg = state["message"].lower()

    company_keywords = [
    "company",
    "about",
    "service",
    "services",
    "help",
    "offer",
    "provide",
    "what do you do",
    "how you help",
    "how u help",
    "business",
    "fly your tech",
    "fyt",
    "location",
    "address",
    "where are you",
    "office",
    "contact"
]


    if any(keyword in msg for keyword in company_keywords):
        return "company"

    if any(x in msg for x in ["lead", "customer", "client"]):
        return "lead"

    if any(x in msg for x in ["schedule", "meeting", "email"]):
        return "schedule"

    return "llm"
