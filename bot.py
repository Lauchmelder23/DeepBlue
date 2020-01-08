import discord
import os
import json
from discord.ext import commands
from util import logging, config

# Bot URL https://discordapp.com/api/oauth2/authorize?client_id=657709911337074698&permissions=314432&scope=bot

total = 0
failed = 0

logging.info("Starting up...\n")
logging.info("--- Loading configs ---\n")
if not config.load("config.json"):
    failed += 1
total += 1

logging.info("Finished loading configs.")
logging.info(f"Total {total}, Failed {failed}\n")



client = commands.Bot(command_prefix=config.settings["prefix"], case_insensitive=True)


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
    logging.info("--- Loading cogs ---\n")
    
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
            except Exception as e:
                logging.info(f"Trying {cog}.....Failed!")
                logging.error(str(e))
                failed += 1


    # Load "api" cogs
    for filename in os.listdir("./cogs/api"):
        if filename.endswith(".py"):
            total += 1
            cog = f"cogs.api.{filename[:-3]}"

            try:
                client.load_extension(cog)
                logging.info(f"Trying {cog}.....Success!")
            except Exception as e:
                logging.info(f"Trying {cog}.....Failed!")
                logging.error(str(e))
                failed += 1

    logging.info("Finished loading cogs.")
    logging.info(f"Total {total}, Failed {failed}\n")

    logging. info("Deep Blue finished loading.")



key = config.settings["client_key"]
client.run(key)