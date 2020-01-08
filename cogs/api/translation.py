import discord
from discord.ext import commands
from util import checking
from api import translation

class Translation(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="translate", description="Translates the given text", usage="translate <ISO CountryCode>", aliases=["tl"])
    @commands.check(checking.is_author_bot)
    async def translate(self, ctx: commands.Context, language: str, *message: str):
        # Get language code
        code = translation.name_to_ISO(language)
        text = ' '.join(message)
        if code == "":
            await ctx.send(f"There is no language named {language}.")
            return
        
        translated = translation.translate(text, code)
        await ctx.send(translated)

def setup(client: discord.Client):
    client.add_cog(Translation(client))