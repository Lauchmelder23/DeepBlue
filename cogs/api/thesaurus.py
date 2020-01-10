import discord
from discord.ext import commands
from api import thesaurus

class Thesaurus(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="thesaurus", description="Makes you smarter.", usage="thesaurus <message>", aliases=["saurus", "thes"])
    @commands.cooldown(1, 3)
    async def thesaurus(self, ctx, *message):
        loading = await ctx.send("Thinking...")
        saurus = thesaurus.thesaurufy_sentence(" ".join(message))
        await loading.edit(content=saurus)

def setup(client):
    client.add_cog(Thesaurus(client))