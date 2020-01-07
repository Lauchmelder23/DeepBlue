import discord

from discord.ext import commands
from api import inspirobot

class Inspirobot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="Inspirobot", description="Sends a randomly generated inspirational quote", aliases=["inspiration", "inspiro"])
    @commands.cooldown(1, 5)
    async def inspirobot(self, ctx):
        image = inspirobot.get_inspirational_quote()
        if image is None:
            await ctx.message.add_reaction("⚠️")
        else:
            embed = discord.Embed(title="InspiroBot", color=0x111387)
            embed.set_image(url=image)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Inspirobot(client))