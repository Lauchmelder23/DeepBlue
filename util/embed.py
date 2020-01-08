import discord
from util import config

def make_error_embed(message: str) -> discord.Embed:
    embed = discord.Embed(title="Error", description=message, colour=int(config.settings["err_color"], 16))
    return embed

def make_embed(title: str, desc: str) -> discord.Embed:
    embed = discord.Embed(title=title, description=desc, colour=int(config.settings["color"], 16))
    return embed

def make_embed_field(title: str, desc: str, field_name: str, field_val: str, inline: bool = True) -> discord.Embed:
    embed = discord.Embed(title=title, description=desc, colour=int(config.settings["color"], 16))
    embed.add_field(name=field_name, value=field_val, inline=inline)
    return embed

def make_embed_fields(title: str, desc: str, *fields: tuple) -> discord.Embed:
    embed = discord.Embed(title=title, description=desc, colour=int(config.settings["color"], 16))
    for name, value in fields:
        embed.add_field(name=name, value=value)
    return embed

    
def make_embed_fields_ninl(title: str, desc: str, *fields: tuple) -> discord.Embed:
    embed = discord.Embed(title=title, description=desc, colour=int(config.settings["color"], 16), inline=False)
    for name, value in fields:
        embed.add_field(name=name, value=value)
    return embed