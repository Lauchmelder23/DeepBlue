'''
This file provides the functionality for
the translation function, by first converting the
country/language name to an ISO369-1 language identifier 
and then translating it using the Yandex Translation API
'''
import requests, urllib.parse
from util import logging, config
import pycountry

api_key = config.settings["api_keys"]["yandex"]
langs = pycountry.languages

def name_to_ISO(name: str) -> str:
    alpha = ""
    for language in langs:
        if language.name.lower() == name.lower():
            try:
                alpha = language.alpha_2
                break
            except:
                logging.warning(f"Tried to get alpha2 code of unknown language {language}")

    return alpha

def ISO_to_name(ISO: str) -> str:
    name = ""
    for language in langs:
        try:
            if language.alpha_2.lower() == ISO.lower():
                try:
                    name = language.name
                    break
                except:
                    logging.warning(f"Tried to get name of unknown language code {ISO}")
        except:
            # i dont care tbh
            pass

    return name

def translate(text: str, lang: str) -> (str, str):
    url_encoded_text = urllib.parse.quote(text)
    url = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={api_key}&text={url_encoded_text}&lang={lang}"

    response = requests.get(url)
    if not response.ok:
        logging.error(f"Failed to contact Yandex API: {response.status_code}")
        return ""
    return (response.json()["text"][0], response.json()["lang"])