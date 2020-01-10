import requests
import re, random
import nltk
from util import logging, config

key = config.settings["api_keys"]["thesaurus"]
url = f"http://thesaurus.altervista.org/thesaurus/v1?key={key}&language=en_US&output=json&word="

def thesaurufy_sentence(sentence):
    symbols = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(symbols)

    if len(symbols) == 0:
        return ""
    
    for i in range(0, len(symbols)):
        if not symbols[i].isalpha():
            continue

        if tags[i][1] != "NN" and tags[i][1] != "VB" and tags[i][1] != "VBG" and tags[i][1] != "VBP" and tags[i][1] != "JJ" and tags[i][1] != "RB":
            symbols[i] = " " + symbols[i]
            continue

        response = requests.get(url + symbols[i])
        if not response.ok:
            # logging.warning(f"Thesaurus API returned {response.status_code} ({url + symbols[i]})")
            symbols[i] = " " + symbols[i]
            continue
        
        responses = response.json()["response"]
        condition = ""
        if tags[i][1] == "JJ":
            condition = "(adj)"
        elif tags[i][1] == "RB":
            condition = "(adv)"
        elif tags[i][1] == "NN":
            condition = "(noun)"
        else:
            condition = "(verb)"

        try:
            words = random.choice([a for a in responses if a["list"]["category"] == condition])["list"]["synonyms"].split("|")
        except:
            symbols[i] = " " + symbols[i]
            continue
        
        # print(words)
        word = words[random.randint(0, len(words) - 1)]
        
        if "(" in word:
            if "antonym" in word.split("(")[1].lower():
                symbols[i] = " " + symbols[i]
                continue

            word = word.split("(")[0][:-1]

        symbols[i] = " " + word

    return "".join(symbols)
