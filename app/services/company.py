from yahooquery import search

def get_symbol(company_name):

    result = search(company_name)

    quotes = result.get("quotes", [])

    if not quotes:
        return None

    return quotes[0]["symbol"]