import discord
import os
import json
from discord.ext import commands
from util import logging

# Bot URL https://discordapp.com/api/oauth2/authorize?client_id=657709911337074698&permissions=314432&scope=bot

client = commands.Bot(command_prefix='.', case_insensitive=True)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("👎")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f"cogs.{extension}")
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("👎")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.reload_extension(f"cogs.{extension}")
        await ctx.message.add_reaction("👍")
    except:
        await ctx.message.add_reaction("👎")


@client.event
async def on_ready():
    logging.info("Starting up...\n")
    logging.info("Trying to load cogs...\n")
    total = 0
    failed = 0
    # Load all cogs on startup
    # Load "fun" cogs
    for filename in os.listdir("./cogs/fun"):
        if filename.endswith(".py"):
            total += 1
            cog = f"cogs.fun.{filename[:-3]}"

            try:
                client.load_extension(cog)
                logging.info(f"Trying {cog}.....Success!")
            except:
                logging.error(f"Trying {cog}.....Failed!")
                failed += 1


    # Load "api" cogs
    for filename in os.listdir("./cogs/api"):
        if filename.endswith(".py"):
            total += 1
            cog = f"cogs.api.{filename[:-3]}"

            try:
                client.load_extension(cog)
                logging.info(f"Trying {cog}.....Success!")
            except:
                logging.error(f"Trying {cog}.....Failed!")
                failed += 1

    logging.info("Finished loading cogs.")
    logging.info(f"Total {total}, Failed {failed}\n")

    logging. info("Deep Blue finished loading.")

with open("config.json", "r") as key_file:
    json = json.load(key_file)
    key = json["client_key"]

client.run(key)