from app.services.finance import get_financial_data
from app.services.company import get_symbol
from app.services.news import get_company_news
from app.services.llm import llm

def company_research_node(state):

    company = state["company"]

    prompt = f"""
    Analyze {company}.

    Provide:
    1. Business Model
    2. Main Products
    3. Industry Position
    4. Competitive Advantages

    Keep it concise.
    """

    response = llm.invoke(prompt)

    return {
        "company_info": response.content
    }

def finance_node(state):

    company = state["company"]

    symbol = get_symbol(company)

    data = get_financial_data(symbol)

    prompt = f"""
    Analyze these financial metrics:

    {data}

    Explain:
    - valuation
    - financial strength
    - investment attractiveness
    """

    response = llm.invoke(prompt)

    return {
        "finance_info": response.content
    }

def news_node(state):

    company = state["company"]

    news_data = get_company_news(company)

    prompt = f"""
    Analyze recent news about {company}.

    News:

    {news_data}

    Summarize:

    - Important developments
    - Opportunities
    - Risks
    - Overall sentiment
    """

    response = llm.invoke(prompt)

    return {
        "news_info": response.content
    }

def risk_node(state):

    prompt = f"""
    Analyze investment risks based on:

    COMPANY ANALYSIS:
    {state['company_info']}

    FINANCIAL ANALYSIS:
    {state['finance_info']}

    NEWS ANALYSIS:
    {state['news_info']}

    Identify:

    1. Financial Risks
    2. Business Risks
    3. Market Risks
    4. Competitive Risks

    Give an overall risk level:
    LOW / MEDIUM / HIGH
    """

    response = llm.invoke(prompt)

    return {
        "risk_analysis": response.content
    }

def decision_node(state):

    prompt = f"""
    Return output in this format:

    Recommendation:
    INVEST/WATCHLIST/PASS

    Confidence:
    0-100

    Top Positives:
    - point
    - point

    Top Risks:
    - point
    - point

    Summary:
    short paragraph
    """

    response = llm.invoke(prompt)

    return {
        "decision": response.content
    }