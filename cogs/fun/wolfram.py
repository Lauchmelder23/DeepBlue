import discord
from discord.ext import commands
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
from util import embed

class WolframAlpha(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = WolframLanguageSession()

    def __del__(self):
        self.session.terminate()

    @commands.command(name="WolframLanguage", description="Evaluates WolframLanguage expressions (Not to be confused with WolframAlpha!)", usage="WolframLanguage <expression>", aliases=["wl"])
    async def WolframLanguage(self, ctx, *expr):
        msg = await ctx.send(embed=embed.make_embed("WolframLanguage", "Thinking..."))
        expr = " ".join(expr)
        evaluate = self.session.evaluate(expr)

        self.session.evaluate(wl.Export("eval.png", evaluate, "PNG"))
        await msg.delete()
        data = embed.make_embed_image("Result", "eval.png")
        await ctx.send(embed=data[0], file=data[1])

def setup(client):
    client.add_cog(WolframAlpha(client))