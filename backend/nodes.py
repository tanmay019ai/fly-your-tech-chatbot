from state import ChatState
from tools.company_info import company_info_tool
from tools.lead_tool import lead_management_tool
from tools.schedule_tool import schedule_email_tool
from llm import call_llm

def router_node(state: ChatState) -> ChatState:
    return state

def company_node(state: ChatState) -> ChatState:
    result = company_info_tool.run(state["message"])
    return {
        "message": state["message"],
        "response": result
    }

def lead_node(state: ChatState) -> ChatState:
    result = lead_management_tool.run(state["message"])
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
