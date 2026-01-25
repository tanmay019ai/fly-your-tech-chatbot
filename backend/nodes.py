from backend.state import ChatState
from backend.tools.company_info import company_info_tool
from backend.tools.lead_tool import lead_tool
from backend.tools.schedule_tool import schedule_email_tool

from backend.llm import call_llm

def router_node(state: ChatState) -> ChatState:
    return state

def company_node(state):
    print("🏢 COMPANY NODE HIT")
    result = company_info_tool.run(state["message"])
    return {
        "message": state["message"],
        "response": result
    }


def lead_node(state: ChatState) -> ChatState:
    result = lead_tool.run(state["message"])
    return {
        "message": state["message"],
        "response": result
    }

def schedule_node(state: ChatState) -> ChatState:
    result = schedule_email_tool.run(state["message"])
    return {
        "message": state["message"],
        "response": result
    }

def llm_node(state: ChatState) -> ChatState:
    reply = call_llm(state["message"])
    return {
        "message": state["message"],
        "response": reply
    }
