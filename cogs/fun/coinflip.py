'''
Flips a coin.
Will probably reworked into a "games" cog to
hold more interactive commands
'''
import discord
import random
from discord.ext import commands

class Coinflip(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="coinflip", description="Flips a coin and reacts with the result", usage="coin", aliases=["coin", "flip"])
    async def coinflip(self, ctx: commands.Context):
        if random.randint(0, 1) == 0:
            await ctx.message.add_reaction("🌑")
        else:
            await ctx.message.add_reaction("🌕")

def setup(client: discord.Client):
    client.add_cog(Coinflip(client))