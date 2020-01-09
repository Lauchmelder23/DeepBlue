import discord
from discord.ext import commands
from util import embed, config
from api import quote

class Quote(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="quote", description="Sends a random quote", usage="quote", aliases=["q"])
    @commands.cooldown(1, 2)
    async def quote(self, ctx: commands.Context):
        please_kill_me = quote.fetch_quote()
        if len(please_kill_me) == 0:
            await ctx.send(embed=embed.make_error_embed("Something went wrong while fetching a random quote"))
            return
        
        end_my_life = discord.Embed(title=f'"{please_kill_me[0]}"', colour=int(config.settings["color"], 16))
        end_my_life.set_footer(text=please_kill_me[1])
        await ctx.send(embed=end_my_life)

def setup(client: discord.Client):
    client.add_cog(Quote(client))