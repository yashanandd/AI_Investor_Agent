from langgraph.graph import StateGraph, END

from app.agent.state import AgentState
from app.agent.nodes import (
    company_research_node,
    finance_node,
    news_node,
    risk_node,
    decision_node
)

builder = StateGraph(AgentState)

builder.add_node(
    "research",
    company_research_node
)

builder.add_node(
    "finance",
    finance_node
)

builder.add_node(
    "news",
    news_node
)

builder.add_node(
    "risk",
    risk_node
)

builder.add_node(
    "decision",
    decision_node
)

builder.set_entry_point(
    "research"
)

builder.add_edge(
    "research",
    "finance"
)

builder.add_edge(
    "finance",
    "news"
)
builder.add_edge(
    "news",
    "risk"
)
builder.add_edge(
    "risk",
    "decision"
)
builder.add_edge(
    "decision",
    END
)

graph = builder.compile()