import json
from util import logging

filepath = ""
settings = {}

def load(file):
    global settings
    filepath = file
    try:
        with open(file, "r") as sett_file:
            settings = json.load(sett_file)
        logging.info(f"Trying {filepath}.....Success!")
        return True
    except Exception as e:
        logging.info(f"Trying {filepath}.....Failed!")
        logging.error(str(e))
        return False
