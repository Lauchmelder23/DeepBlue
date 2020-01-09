import discord
from discord.ext import commands

class Responses(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # @applesauce
        if ("<@!568271450176356352>" in message.content) and ("<@!657709911337074698>" in message.content):
            await message.channel.send(f"Stop pinging us {message.author.mention} <:pinged:451198700832817202>")
            return

        if "<@!657709911337074698>" in message.content:    
            await message.channel.send(f"{message.author.mention} <:pinged:451198700832817202>")
            return

def setup(client):
    client.add_cog(Responses(client))