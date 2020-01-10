import requests
import re, random
from util import logging, config

key = config.settings["api_keys"]["thesaurus"]
url = f"http://thesaurus.altervista.org/thesaurus/v1?key={key}&language=en_US&output=json&word="

def thesaurufy_sentence(sentence):
    symbols = re.findall(r"[\w']+|[.,!?;]", sentence)

    if len(symbols) == 0:
        return ""
    
    for i in range(0, len(symbols)):
        if not symbols[i].isalpha():
            continue

        response = requests.get(url + symbols[i])
        if not response.ok:
            # logging.warning(f"Thesaurus API returned {response.status_code} ({url + symbols[i]})")
            symbols[i] = " " + symbols[i]
            continue
        
        responses = response.json()["response"]
        words = responses[random.randint(0, len(responses) - 1)]["list"]["synonyms"].split("|")
        word = words[random.randint(0, len(words) - 1)]
        
        if "(" in word:
            if "antonym" in word.split("(")[1].lower():
                symbols[i] = " " + symbols[i]
                continue
            
            word = word.split("(")[0][:-1]

        symbols[i] = " " + word

    return "".join(symbols)
