import requests
import random
from util import logging

def fetch_quote() -> tuple:
    url = "https://favqs.com/api/qotd"
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Failed to access Quotes API: {response.status_code} [{url}]")
        return ()

    data = response.json()
    return (data["quote"]["body"], data["quote"]["author"])