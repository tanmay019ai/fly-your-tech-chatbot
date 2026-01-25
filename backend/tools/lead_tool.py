from langchain.tools import tool
import json

@tool
def lead_tool(query: str) -> str:
    """
    Returns existing leads.
    """
    leads = [
        {
            "name": "Rahul Sharma",
            "email": "rahul@example.com",
            "service": "Web Development"
        },
        {
            "name": "Anita Verma",
            "email": "anita@example.com",
            "service": "AI Chatbot"
        }
    ]
    return json.dumps(leads, indent=2)
