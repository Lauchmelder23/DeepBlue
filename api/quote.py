import requests
import random
from util import logging

def fetch_quote() -> tuple:
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Failed to access Quotes API: {response.status_code} [{url}]")
        return ()

    data = response.json()
    return (data["quoteText"], data["quoteAuthor"])