from langgraph.graph import StateGraph, END

from app.agent.state import AgentState
from app.agent.nodes import company_research_node

builder = StateGraph(AgentState)

builder.add_node(
    "research",
    company_research_node
)

builder.set_entry_point(
    "research"
)

builder.add_edge(
    "research",
    END
)

graph = builder.compile()