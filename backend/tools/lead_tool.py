import json
from langchain.tools import tool

@tool
def lead_management_tool(query: str) -> str:
    """
    Fetches existing leads and their interested services.
    """
    with open("data/leads.json", "r") as f:
        leads = json.load(f)

    return json.dumps(leads, indent=2)
