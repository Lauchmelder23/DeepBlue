import discord
from discord.ext import commands
from util import logging, checking
import re

class AutoConvert(commands.Cog):

    def __init__(self, client):
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

    def convert_currency(self, _from, to, value):
        if _from == '€':
            conversion_rate = self.currency_conversion[_from + to]
        elif to == '€':
            conversion_rate = 1/self.currency_conversion[to + _from]
        else:
            conversion_rate = self.currency_conversion['€' + to] / self.currency_conversion['€' + _from]

        return round(value * conversion_rate, 2)
                
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        empty = True

        currencies = self.contains_currency(message)
        embed = discord.Embed(title="Here are some useful conversions:", color=0x111387)

        if len(currencies) != 0:
            empty = False
            for element in currencies:
                currency_string = ""
                for currency in self.currencies:
                    if currency == element[1]:
                        continue
                    currency_string += f"{self.convert_currency(element[1], currency, element[0])}{currency}, "
                embed.add_field(name=str(element[0])+element[1], value=currency_string[:-2])

        

        if not empty:
            await message.channel.send(embed=embed)




def setup(client):
    client.add_cog(AutoConvert(client))