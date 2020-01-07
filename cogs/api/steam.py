import discord
from discord.ext import commands
from api import steam

class Steam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="SteamLevel", description="Finds the steam level of a user", usage="SteamLevel <Vanity URL>",  aliases=["level"])
    @commands.cooldown(1, 2)
    async def SteamLevel(self, ctx, vanity_url):
        level = steam.get_steam_level(vanity_url)
        
        if level is None:
            await ctx.send(f"There is nobody named \"{vanity_url}\" on Steam, or their profile might be pivate.")
        else:
            percentile = round(float(steam.get_steam_level_distribution(level)), 2)
            await ctx.send(f"{vanity_url} is level {level}! This makes him better than {percentile}% of Steam users!")
            



def setup(client):
    client.add_cog(Steam(client))