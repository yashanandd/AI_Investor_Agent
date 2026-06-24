from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    company: str
    company_analysis: str
    financial_analysis: str
    news_analysis: str
    risk_analysis: str
    investment_decision: str