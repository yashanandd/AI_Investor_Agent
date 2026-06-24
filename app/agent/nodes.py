from app.services.gemini import llm

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