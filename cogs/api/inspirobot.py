'''
This is the cog that allows users to
fetch an AI-generated inspirational quote
made by Inspirobot
'''
import discord

from discord.ext import commands
from api import inspirobot
from util import config

class Inspirobot(commands.Cog):

    def __init__(self, client : discord.Client):
        self.client = client

    @commands.command(name="inspirobot", description="Sends a randomly generated inspirational quote", usage="inspirobot", aliases=["inspiration", "inspiro", "insp"])
    @commands.cooldown(1, 5)
    async def inspirobot(self, ctx : commands.Context):
        image = inspirobot.get_inspirational_quote()
        if image is None:
            await ctx.message.add_reaction("⚠️")
        else:
            embed = discord.Embed(title="InspiroBot", color=int(config.settings["color"], 16))
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @commands.command(name="test", dscription="Who cares tbh")
    @commands.cooldown(1, 3)
    async def test(self, ctx):
        await self.client.get_channel(621378664977793024).send("Test")
        await ctx.send(self.client.name)

def setup(client : discord.Client):
    client.add_cog(Inspirobot(client))
