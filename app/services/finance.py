import yfinance as yf

def get_financial_data(company_symbol):

    stock = yf.Ticker(company_symbol)

    info = stock.info

    return {
        "company": info.get("longName"),
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow")
    }