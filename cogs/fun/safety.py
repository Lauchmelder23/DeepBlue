import discord
from discord.ext import commands
from util import embed, logging
import time

class Safety(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.msg_buffer = [".", ".", ".", ".", ".", "."]
        self.ping = "<@&380535423233032193>"
        self.channel = 439466964625391637
        self.last_action = 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.channel:
            return

        if (time.time() - self.last_action) < 10:
            return
    

        if self.ping in message.content:
            for msg in self.msg_buffer:
                if self.ping in msg:
                    # Ping not adequately spaced
                    await message.channel.send(embed=embed.make_embed("Coronavirus Safety Information", "Due to the ongoing pandemic, please remember to space your NaughtyStep pings at least six messages apart.\n Thank you."))
                    self.last_action = time.time()
                    break

        self.msg_buffer.pop(0)
        self.msg_buffer.append(message.content)
        
def setup(client):
    client.add_cog(Safety(client))