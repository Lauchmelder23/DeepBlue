'''
A module that sits between the API and the cog
and provides functions for easy communication
with the Steam API
'''
import requests
import json
from util import logging, config

key = config.settings["api_keys"]["steam"]

# Returns a (hopefully) valid Steam API URL
def assemble_url(interface_name: str, method_name: str, version: int) -> str:
    return f"http://api.steampowered.com/{interface_name}/{method_name}/v{version}/?key={key}&format=json"

def get_json_request_response(url: str):
    response = requests.get(url)

    if not response.ok:
        logging.error(f"Steam API response not OK: {response.status_code} [{url}]")
        return None

    json = response.json()
    return json

# Finds the SteamID of a user by their Vanity URL
def resolve_vanity_url(vanity_url: str) -> str:
    url = assemble_url("ISteamUser", "ResolveVanityURL", 1) + f"&vanityurl={vanity_url}"
    json = get_json_request_response(url)

    success = json["response"]["success"]
    if success != 1:
        logging.error(f"Something went wrong while resolving Vanity URL: {success}")
        return None

    return json["response"]["steamid"]


# Gets a users steam level
def get_steam_level(vanity_url: str) -> str:
    steamid = resolve_vanity_url(vanity_url)
    if steamid is None:
        logging.error("Could not resolve Vanity URL")
        return None

    url = assemble_url("IPlayerService", "GetSteamLevel", 1) + f"&steamid={steamid}"
    json = get_json_request_response(url)
    
    if len(json["response"]) == 0:
        return None

    return json["response"]["player_level"]

# Gets the percentage of players who have a lower level
def get_steam_level_distribution(level: str) -> str:
    url = assemble_url("IPlayerService", "GetSteamLevelDistribution", 1) + f"&player_level={level}"
    json = get_json_request_response(url)

    if len(json["response"]) == 0:
        return None

    return json["response"]["player_level_percentile"]