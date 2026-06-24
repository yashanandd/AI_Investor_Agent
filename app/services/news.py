import requests

def get_company_news(company):

    url = f"https://news.google.com/rss/search?q={company}"

    response = requests.get(url)

    return response.text[:3000]