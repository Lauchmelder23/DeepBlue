import discord
from discord.ext import commands
import re
from datetime import datetime

class Logger(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.first = True
        self.last_update = datetime.now()
        self.most_common = []

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.channel.id != 439466964625391637:
            return

        if message.content.startswith(('.', '!', '-', '?', '/')):
            return

        with open('data/naughty_step.txt', 'a') as file:
            file.write(message.content + '\n')
            
        
def setup(client):
    client.add_cog(Logger(client))
