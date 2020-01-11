import discord
import time
import asyncio
from discord.ext import commands
from datetime import datetime, timedelta
from random import randrange
from util import logging

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
        self.threads = 0
        self.THREAD_LIMIT = 20

    async def call_event(self, sleep_time: int, name: str, user: discord.User, channel: discord.TextChannel):
        await asyncio.sleep(sleep_time)
        await channel.send(f"{user.mention} Your event \"{name}\" starts now!")
        self.threads -= 1

    @commands.command(name="schedule", description="Schedules an event", usage="schedule <name>", aliases=["s"])
    @commands.cooldown(1, 3)
    async def schedule(self, ctx: commands.Context, *name: str):
        date = ceil_dt(random_date(datetime.now(), datetime.now() + timedelta(days=7)), timedelta(minutes=15))
        await ctx.send(f"I scheduled \"{' '.join(name)}\" for **{date.strftime('%d.%m.%Y %H:%M CET')}**")

        if self.threads <= self.THREAD_LIMIT:
            seconds = (date - datetime.now()).seconds
            await self.call_event(seconds, ' '.join(name), ctx.message.author, ctx.message.channel)
            self.threads += 1
            logging.info(f"Scheduled new event in {seconds} seconds. Current events: {self.threads}")
        else:
            logging.warning("Schedule: Event limit reached. Async function was not called.")



def setup(client: discord.Client):
    client.add_cog(Schedule(client))
