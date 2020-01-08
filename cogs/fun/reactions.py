import discord
from discord.ext import commands

class Reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message : discord.Message):
        if message.author.bot:
            return

        if "canada" in message.content.lower():
            await message.add_reaction("🇨🇦")

        if "germany" in message.content.lower():
            await message.add_reaction("🇩🇪")

        if "uk" in message.content.lower() or "britain" in message.content.lower():
            await message.add_reaction("🇬🇧")

        if "china" in message.content.lower():
            await message.add_reaction("🇨🇳")

        if "america" in message.content.lower() or " usa" in message.content.lower():
            await message.add_reaction("🇬")
            await message.add_reaction("🇦")
            await message.add_reaction("🇾")

        if "extremejoy" in str(message):
            message.add_reaction(664251611765407745)


def setup(client):
    client.add_cog(Reactions(client))