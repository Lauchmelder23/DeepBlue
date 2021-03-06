'''
A module that sits between the API and the cog
and provides functions for easy communication
with the NASA API
'''
import requests
from util import config, logging

api_key = config.settings["api_keys"]["nasa"]

def image_of_the_day() -> str:
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    
    if not response.ok:
        logging.error(f"Failed to fetch Image of the day (NASA API): {response.status_code}")
        return

    image_link = response.json()["hdurl"]
    return image_link