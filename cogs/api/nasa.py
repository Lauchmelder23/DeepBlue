'''
This cog is capable of communicating with the
NASA API
'''
import discord
from discord.ext import commands
from api import nasa
from util import config

class Nasa(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="apod", description="Posts NASA's picture of the day.", usage="apod")
    @commands.cooldown(1, 30)
    async def apod(self, ctx: commands.Context):
        url = nasa.image_of_the_day()
        embed = discord.Embed(title="Astronomy Picture of the day", color=int(config.settings["color"], 16))
        embed.set_image(url=url)

        await ctx.send(embed=embed)


def setup(client: discord.Client):
    client.add_cog(Nasa(client))