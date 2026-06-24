from app.services.finance import get_financial_data
from app.services.company import get_symbol
from app.services.news import get_company_news
from app.services.llm import llm


def company_research_node(state):

    company = state["company"]

    prompt = f"""
    Analyze {company}.

    Return exactly:

    Business Model:
    - point

    Main Products:
    - point
    - point

    Industry Position:
    - point

    Competitive Advantages:
    - point
    - point

    Verdict:
    - one sentence

    Maximum 80 words.
    Use bullet points only.
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

    Return exactly:

    Valuation:
    - point

    Financial Strength:
    - point
    - point

    Growth Potential:
    - point

    Investment Attractiveness:
    - one sentence

    Maximum 100 words.
    Use bullet points only.
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

    Return exactly:

    Key Developments:
    - point
    - point
    - point

    Opportunities:
    - point

    Risks:
    - point

    Sentiment:
    Positive / Neutral / Negative

    Maximum 100 words.
    Use bullet points only.
    """

    response = llm.invoke(prompt)

    return {
        "news_info": response.content
    }


def risk_node(state):

    prompt = f"""
    Analyze investment risks.

    COMPANY:
    {state['company_info']}

    FINANCIALS:
    {state['finance_info']}

    NEWS:
    {state['news_info']}

    Return exactly:

    Risk Level:
    LOW / MEDIUM / HIGH

    Financial Risks:
    - point

    Business Risks:
    - point

    Market Risks:
    - point

    Competitive Risks:
    - point

    Summary:
    - one sentence

    Maximum 100 words.
    Use bullet points only.
    """

    response = llm.invoke(prompt)

    return {
        "risk_analysis": response.content
    }


def decision_node(state):

    prompt = f"""
    You are a professional investment analyst.

    Company Analysis:
    {state['company_info']}

    Financial Analysis:
    {state['finance_info']}

    News Analysis:
    {state['news_info']}

    Risk Analysis:
    {state['risk_analysis']}

    Return exactly:

    Recommendation:
    INVEST / WATCHLIST / PASS

    Confidence:
    XX

    Key Strengths:
    - point
    - point
    - point

    Key Risks:
    - point
    - point
    - point

    Summary:
    one short sentence

    Maximum 120 words.
    Use bullet points only.
    """

    response = llm.invoke(prompt)

    return {
        "decision": response.content
    }