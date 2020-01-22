import discord
from discord.ext import commands
from util import embed

class Encryption(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
    
    @commands.command(name="rot", description="Applies the ROT encryption", usage="rot [number] [message]")
    @commands.cooldown(1, 2)
    async def rot(self, ctx: commands.Context, shift: str, *message: str):
        if not shift.isnumeric():
            await ctx.send(embed=embed.make_error_embed(f"{shift} is not a number."))
            return

        shift = int(shift)
        if (shift < 1) or (shift > 25):
            await ctx.send(embed=embed.make_error_embed("That's too much rotation. Stop it."))
            return
        
        old_message = list(' '.join(message))
        for i in range(0, len(old_message)):
            if not old_message[i].isalpha():
                continue

            if old_message[i].isupper():
                old_message[i] = chr(ord('A') + ((ord(old_message[i]) + shift - ord('A')) % 26))
            else:
                old_message[i] = chr(ord('a') + ((ord(old_message[i]) + shift - ord('a')) % 26))

        await ctx.send(''.join(old_message))

def setup(client: discord.Client):
    client.add_cog(Encryption(client))