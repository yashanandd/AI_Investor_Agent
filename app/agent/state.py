from typing import TypedDict

class AgentState(TypedDict, total=False):
    company: str
    company_info: str
    finance_info: str
    news_info: str
    risk_analysis: str
    decision: str