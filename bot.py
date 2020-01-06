import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

client.run()