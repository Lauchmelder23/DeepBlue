import requests
import numpy as np 
import matplotlib.pyplot as plt
import datetime
from util import logging

def current_level() -> []:
    url = "https://api.carbonintensity.org.uk/intensity"
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Failed to access Carbon API: {response.status_code} [{url}]")

    data = response.json()["data"][0]
    return [data["from"], data["intensity"]["forecast"], data["intensity"]["actual"], data["intensity"]["index"]]

def level_at(date: str) -> []:
    url = f"https://api.carbonintensity.org.uk/intensity/date/{date}"
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Failed to access Carbon API: {response.status_code} [{url}]")
        return []

    if len(response.json()["data"]) == 0:
        return []

    data = response.json()["data"][0]
    return [data["from"], data["intensity"]["forecast"], data["intensity"]["actual"], data["intensity"]["index"]]

def level_from_to(start: str, stop: str) -> str:
    url = f"https://api.carbonintensity.org.uk/intensity/{start}/{stop}"
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Failed to access Carbon API: {response.status_code} [{url}]")
        return ""

    if len(response.json()["data"]) == 0:
        return []

    data = response.json()["data"]

    x = []
    measured = []
    indices = []

    for i in range(len(data)):
        intensity = data[i]["intensity"]
        x.append(datetime.datetime.strptime(data[i]["from"], "%Y-%m-%dT%H:%MZ"))
        measured.append(intensity["actual"])
        indices.append(intensity["index"])

    curr_color = indices[0]
    curr_color_index = 0
    for i in range(len(measured)):
        if indices[i] != curr_color:
            color = ""
            if curr_color == "very low":
                color = "#5bcc32"
            if curr_color == "low":
                color = "#87cc32"
            if curr_color == "moderate":
                color = "#ccc932"
            if curr_color == "high":
                color = "#cc8e32"
            if curr_color == "very high":
                color = "#cc4f32"

            plt.plot(x[curr_color_index:i+1], measured[curr_color_index:i+1], color)
            curr_color_index = i
            curr_color = indices[i]

    plt.xlabel("Time & Date")
    plt.ylabel("Carbon Intensity [gCO2/kWh]")
    plt.xticks(rotation=45)
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.grid(b=True)
    plt.savefig("plot.png")
    plt.clf()
    return "plot.png"