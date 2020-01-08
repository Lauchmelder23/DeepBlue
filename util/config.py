'''
This module loads settings. Right now
it can only hold one config file at a time
'''

import json
from util import logging

filepath = ""
settings = {}

def load(file : str) -> bool:
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
