import discord
from discord.ext import commands
from datetime import datetime, timedelta
from random import randrange

def ceil_dt(dt, delta):
    return dt + (datetime.min - dt) % delta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


class Schedule(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client

    @commands.command(name="schedule", description="Schedules an event", usage="schedule <name>", aliases=["s"])
    @commands.cooldown(1, 3)
    async def schedule(self, ctx: commands.Context, *name: str):
        await ctx.send(f"I scheduled \"{' '.join(name)}\" for **{ceil_dt(random_date(datetime.now(), datetime.now() + timedelta(days=7)), timedelta(minutes=15)).strftime('%d.%m.%Y %H:%M GMT')}**")

def setup(client: discord.Client):
    client.add_cog(Schedule(client))