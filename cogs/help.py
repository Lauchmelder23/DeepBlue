import discord
from discord.ext import commands
from util import config, embed, logging

class SetupHelp(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self._original_help_command = client.help_command
        client.help_command = Help()
        client.help_command.cog = self

class Help(commands.MinimalHelpCommand):
    async def command_not_found(self, string: str):
        await self.context.send(embed=embed.make_error_embed("Command not found"))

    async def subcommand_not_found(self, command, string):
        await self.context.send(embed=embed.make_error_embed("Command not found"))

    async def send_cog_help(self, cog):
        await self.context.send(embed=embed.make_error_embed("Command not found"))

    async def send_group_help(self, group):
        await self.context.send(embed=embed.make_error_embed("Command not found"))

    async def send_command_help(self, command):
        try:
            alias = ""
            if command.aliases != []:
                for i in range(len(command.aliases)):
                    if i == len(command.aliases) - 1:
                        alias = alias + '`' + command.aliases[i] + '`'
                    else:
                        alias = alias + '`' + command.aliases[i] + '`' + ', '
            else:
                alias = "`None`"
            
            await self.context.send(embed=embed.make_embed_fields_ninl(command.name, command.description, ("Usage", f"`{config.settings['prefix']}{command.usage}`"), ("Aliases", alias)))
        except Exception as e:
            logging.error(str(e))
            await self.context.send(embed=embed.make_error_embed("Command not found"))

    
    async def send_bot_help(self, mapping):
        # get list of commands
        cmds = []
        prefix = config.settings['prefix']

        for cog, cog_commands in mapping.items():
            cmds = cmds + cog_commands

        newCmds = []
        for item in cmds:
            newCmds.append(str(item))
        newCmds = sorted(newCmds)

        finalCmds = []
        for item in newCmds:
            try:
                finalCmds.append(item)
            except:
                pass

        cmdString = ""
        if len(finalCmds) != 0:
            for i in range(len(finalCmds)):
                if i == len(finalCmds)-1:
                    cmdString = cmdString + '`' + finalCmds[i] + '`'
                else:
                    cmdString = cmdString + '`' + finalCmds[i] + '`' + ', '


        if cmdString != "":
            await self.context.send(embed=embed.make_embed_field('Help', f'To get further information about a command use `{prefix}help <Command>`', "Commands", cmdString, inline=False))
        else:
            await self.context.send(embed=embed.make_error_embed("No commands found."))
        
        

def setup(client: discord.Client):
    client.add_cog(SetupHelp(client))