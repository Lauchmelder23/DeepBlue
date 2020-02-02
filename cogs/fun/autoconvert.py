'''
Listens for certain keywords in messages and
then provides conversion charts that might be
useful.
'''
import discord
from discord.ext import commands
from util import logging, checking, config
import re

class AutoConvert(commands.Cog):

    def __init__(self, client: discord.Client):
        self.client = client
        self.currencies = ['€', '$', '£']
        self.currency_conversion = {
            "€$":1.1144,
            "€£":0.85
        }

    '''
        Checks wether a message contains currency symbols
        Returns an array of prices found

        €, $, £
    '''
    def contains_currency(self, message : discord.Message) -> []:
        prices = []
        words = message.content.split(' ')
        for word in words:
            for currency in self.currencies:
                if currency in word:
                    try:
                        prices.append([float(re.findall(r"[-+]?\d*\.\d+|\d+", word)[0]), currency])
                    except:
                            pass
                    break

        return prices

    def convert_currency(self, _from: str, to: str, value: float) -> float:
        if _from == '€':
            conversion_rate = self.currency_conversion[_from + to]
        elif to == '€':
            conversion_rate = 1/self.currency_conversion[to + _from]
        else:
            conversion_rate = self.currency_conversion['€' + to] / self.currency_conversion['€' + _from]

        return round(value * conversion_rate, 2)
                
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        empty = True

        currencies = self.contains_currency(message)
        embed = discord.Embed(title="Here are some useful conversions:", color=int(config.settings["color"], 16))

        if len(currencies) != 0:
            empty = False
            for element in currencies:
                currency_string = ""
                for currency in self.currencies:
                    if currency == element[1]:
                        continue
                    currency_string += f"{currency}{self.convert_currency(element[1], currency, element[0])}, "
                embed.add_field(name=element[1]+str(element[0]), value=currency_string[:-2])

        if not empty:
            await message.channel.send(embed=embed)


def setup(client: discord.Client):
    client.add_cog(AutoConvert(client))
