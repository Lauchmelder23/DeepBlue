import discord
from discord.ext import commands
from util import checking, embed
from api import translation

class Translation(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="translate", description="Translates the given text", usage="translate <Language> <Text>", aliases=["tl"])
    @commands.check(checking.is_author_bot)
    async def translate(self, ctx: commands.Context, language: str, *message: str):
        # Get language code
        code = translation.name_to_ISO(language)
        text = ' '.join(message)
        if code == "":
            await ctx.send(embed=embed.make_error_embed(f"There is no language named **{language}**."))
            return
        
        response = translation.translate(text, code)
        if len(response) == 0:
            await ctx.send(embed=embed.make_error_embed(f"The translation API doesn't support **{language}**."))
            return
        translated = response[0]
        direction = response[1].split("-")
        _from = translation.ISO_to_name(direction[0])
        _to = translation.ISO_to_name(direction[1])
        await ctx.send(embed=embed.make_embed_field(f"{_from} -> {_to}", None, text, translated))

def setup(client: discord.Client):
    client.add_cog(Translation(client))