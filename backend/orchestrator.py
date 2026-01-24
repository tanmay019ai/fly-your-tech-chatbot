from router import is_company_question
from tools.company_info import company_info_tool

def handle_message(message: str) -> str:
    if is_company_question(message):
        return company_info_tool.run(message)

    return "This will be handled by the LLM later."
