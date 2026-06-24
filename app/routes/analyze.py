from fastapi import APIRouter

from app.agent.graph import graph
from app.models.request import AnalyzeRequest
from app.models.response import AnalyzeResponse

router = APIRouter()

@router.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(data: AnalyzeRequest):

    result = graph.invoke(
        {
            "company": data.company
        }
    )

    return {
        "company": data.company,
        "company_analysis": result["company_info"],
        "financial_analysis": result["finance_info"],
        "news_analysis": result["news_info"],
        "risk_analysis": result["risk_analysis"],
        "investment_decision": result["decision"]
    }
