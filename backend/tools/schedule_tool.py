from langchain.tools import tool

@tool
def schedule_email_tool(query: str) -> str:
    """
    Simulates scheduling an email or meeting.
    """
    return "Meeting scheduled successfully for tomorrow at 2 PM."
