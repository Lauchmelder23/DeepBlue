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

        if message.author.id == 478006431589728259:
            if message.content == "<@&380535423233032193> NUMBERS REEEEEEEE":
                await message.channel.send(f"<@&380535423233032193> {message.author.mention} REEEEEEEE")

            if message.content == "<@&380535423233032193> <:nockgun:352019166288543745> 🔢":
                await message.channel.send(f"<@&380535423233032193> <:nockgun:352019166288543745> {message.author.mention}")

            if message.content == "<@&380535423233032193> is NOT for numbers":
                await message.channel.send(f"<@&380535423233032193> ***IS*** for numbers")
                
def setup(client):
    client.add_cog(Responses(client))