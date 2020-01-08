'''
This module will provide permission checks
for the command executions.
'''

import discord
from discord.ext import commands
from util import logging

def is_author_bot(ctx : commands.Context) -> bool:
    if ctx.message.author.bot:
        return False
    return True