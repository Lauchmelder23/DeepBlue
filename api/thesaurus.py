import requests
import re, random
import nltk
import threading, queue
from util import logging, config

key = config.settings["api_keys"]["thesaurus"]
url = f"http://thesaurus.altervista.org/thesaurus/v1?key={key}&language=en_US&output=json&word="

def start_thread(target, args):
    q = queue.Queue()
    def wrapper():
        q.put(target(args))
    t = threading.Thread(target=wrapper)
    t.start()
    return q

def thesaurufy_sentence(sentence):
    symbols = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(symbols)

    if len(symbols) == 0:
        return ""
    
    queues = []
    for i in range(0, len(symbols)):
        queues.append(start_thread(target = handle_token, args=(tags[i])))
        
    for i in range(0, len(symbols)):
        symbols[i] = queues[i].get()

    return "".join(symbols)

def handle_token(args):
    token = args
    if not token[0].isalpha():
        return token[0]

    if token[1] != "NN" and token[1] != "VB" and token[1] != "VBG" and token[1] != "VBP" and token[1] != "JJ" and token[1] != "RB":
        return (" " + token[0])

    response = requests.get(url + token[0])
    if not response.ok:
        # logging.warning(f"Thesaurus API returned {response.status_code} ({url + token[0]})")
        return (" " + token[0])
    
    responses = response.json()["response"]
    condition = ""
    if token[1] == "JJ":
        condition = "(adj)"
    elif token[1] == "RB":
        condition = "(adv)"
    elif token[1] == "NN":
        condition = "(noun)"
    else:
        condition = "(verb)"

    try:
        words = random.choice([a for a in responses if a["list"]["category"] == condition])["list"]["synonyms"].split("|")
    except:
        return (" " + token[0])
    
    # print(words)
    word = words[random.randint(0, len(words) - 1)]
    
    if "(" in word:
        if "antonym" in word.split("(")[1].lower():
            return (" " + token[0])

        word = word.split("(")[0][:-1]

    return (" " + word)