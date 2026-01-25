from langchain.tools import tool

@tool
def company_info_tool(query: str) -> str:
    """
    Returns Fly Your Tech company information.
    """
    return """
Company Name: Fly Your Tech
Address: India
Phone: +91-XXXXXXXXXX
Email: contact@flyyourtech.com
Services: Web Development, AI Solutions, Cloud Services
Starting Price: ₹25,000
"""
