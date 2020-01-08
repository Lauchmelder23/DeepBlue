import discord
from discord.ext import commands
from api import carbon
from util import embed

class Carbon(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.group(name="carbon", usage="carbon [subcommand]", description="Can accumulate data about carbon levels in the UK")
    @commands.cooldown(1, 5)
    async def carbon(self, ctx):
        pass

    @carbon.command(name="now", usage="carbon now", description="Gets the latest available carbon intensity data")
    async def now(self, ctx):
        data = carbon.current_level()
        await ctx.send(embed=embed.make_embed_fields_footer("Carbon intensity in the UK", f"The current carbon intensity is considered **{data[3]}**.", f"{data[0]} | All values in gCO2/kWh", ("Measured", data[2]), ("Predicted", data[1])))

    @carbon.command(name="at", usage="carbon at <Date>", description="Gets the carbon levels at the given date (YYYY-MM-DD)")
    async def at(self, ctx: discord.Client, date: str):
        data = carbon.level_at(date)
        if len(data) == 0:
            await ctx.send(embed=embed.make_error_embed(f"There is no data available for {date}."))
        else:
            await ctx.send(embed=embed.make_embed_fields_footer("Carbon intensity in the UK", f"The carbon intensity for that date is considered **{data[3]}**.", f"{data[0]} | All values in gCO2/kWh", ("Measured", data[2]), ("Predicted", data[1])))

    @carbon.command(name="during", usage="carbon during <Start> <Stop>", description="Creates a diagram about carbon levels in the given time period (YYYY-MM-DD)")
    @commands.cooldown(1, 25)
    async def during(self, ctx: discord.Client, start: str, stop: str):
        path = carbon.level_from_to(start, stop)
        if path == "":
            await ctx.send(embed=embed.make_error_embed(f"There is no data available for the given time period."))
        else:
            data = embed.make_embed_image("Carbon intensity in the UK", path)
            await ctx.send(embed=data[0], file=data[1])

def setup(client: discord.Client):
    client.add_cog(Carbon(client))