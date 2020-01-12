import discord
from discord.ext import commands
from sympy import preview
from util import embed

class Math(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="latex", description="Transforms a latex(math!) expression to an image", usage="latex <latex>", aliases=["lat", "tex", "l"])
    @commands.cooldown(1, 5)
    async def latex(self, ctx: commands.Context, *expr: str):
        preview(f"$${' '.join(expr)}$$", viewer='file', filename='latex.png', euler=False)
        result = embed.make_embed_image("LaTeX", "latex.png")
        await ctx.send(embed=result[0], file=result[1])


def setup(client: discord.Client):
    client.add_cog(Math(client))