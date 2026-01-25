from langgraph.graph import StateGraph, END
from backend.state import ChatState
from backend.nodes import (
    router_node,
    company_node,
    lead_node,
    schedule_node,
    llm_node,
)
from backend.router import route_condition

graph = StateGraph(ChatState)

graph.add_node("router", router_node)
graph.add_node("company", company_node)
graph.add_node("lead", lead_node)
graph.add_node("schedule", schedule_node)
graph.add_node("llm", llm_node)

graph.add_conditional_edges(
    "router",
    route_condition,
    {
        "company": "company",
        "lead": "lead",
        "schedule": "schedule",
        "llm": "llm",
    }
)

graph.set_entry_point("router")

graph.add_edge("company", END)
graph.add_edge("lead", END)
graph.add_edge("schedule", END)
graph.add_edge("llm", END)

chat_graph = graph.compile()
