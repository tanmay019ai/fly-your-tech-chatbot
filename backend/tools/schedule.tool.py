from langchain.tools import tool

@tool
def schedule_email_tool(query: str) -> str:
    """
    Simulates scheduling an email for a meeting or follow-up.
    """
    return "Email scheduled successfully for the requested date and time."
