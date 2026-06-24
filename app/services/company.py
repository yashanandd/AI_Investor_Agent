COMPANY_SYMBOLS = {
    "tesla": "TSLA",
    "apple": "AAPL",
    "microsoft": "MSFT",
    "nvidia": "NVDA",
    "amazon": "AMZN",
    "google": "GOOGL",
    "meta": "META"
}

def get_symbol(company_name):

    return COMPANY_SYMBOLS.get(
        company_name.lower()
    )