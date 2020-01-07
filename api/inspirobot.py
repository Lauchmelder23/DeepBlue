import requests
from util import logging

def get_inspirational_quote() -> str:
    response = requests.get("http://inspirobot.me/api?generate=true")

    if not response.ok:
        logging.error(f"Steam API response not OK: {response.status_code} [http://inspirobot.me/api?generate=true]")
        return None

    return response.text
