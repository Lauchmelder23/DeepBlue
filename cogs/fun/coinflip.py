import discord
import random
from discord.ext import commands

class Coinflip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="coinflip", description="Flips a coin and reacts with the result", aliases=["coin", "flip"])
    async def coinflip(self, ctx):
        if random.randint(0, 1) == 0:
            await ctx.message.add_reaction("🌑")
        else:
            await ctx.message.add_reaction("🌕")

def setup(client):
    client.add_cog(Coinflip(client))