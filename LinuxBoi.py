#!/usr/bin/env python3

"""
LinuxBoi - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import os
from datetime import datetime
import discord
from itertools import cycle
from discord.ext import commands, tasks

# client = commands.Bot("l!", owner_id=54681233121306214, case_insensitive=False, self_bot=True)
client = commands.Bot("l!", owner_id=546812331213062144, case_insensitive=False)
status = cycle([f'Linux videos | l!help', 'FOSS software | l!help', 'Windows getting worse',
                'Server members | l!help', 'Cryptocurrency | l!help', 'Linux getting popular'])
line_divide = "\n———————————————————————————————"

linuxboi_token = os.environ.get('linuxboi_token')

cogs = [
    "Fun",
    "Information",
    "Linuxinfo",
    "Meme",
    "Moderation",
    "Owner",
    "Utility",
    "Images",
    "Music"
]


class LinuxBoi(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="l!", owner_id=546812331213062144, reconnect=True, case_insensitive=False)

        self.embed_color = 0xF15A24

        self.load_extension('jishaku')
        self.remove_command('help')

    async def on_ready(self):
        # change_status.start()
        await self.change_presence(activity=discord.Activity(type=3, name="Linux videos! | l!help"))

        if not hasattr(self, 'uptime'):
            self.uptime = datetime.utcnow()

        try:
            for cog in cogs:
                self.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(f"Could not load extension {e}")

        print(f"---------------LinuxBoi-----------------------"
              f"\nBot is online and connected to {self.user}"
              f"\nCreated by TrackRunny#3900 on Discord"
              f"\nConnected to {(len(self.guilds))} Guilds."
              f"\n----------------------------------------------")


@client.event()
async def on_message(message):
    if message.content in ("<@554841921185382400>", "@LinuxBoi"):
        await message.channel.send("( :wave: ) → Hello, run `l!commands` to see all my commands!")
    if not message.author.bot:
        await client.process_commands(message)


@commands.is_owner()
@client.command()
async def message_all(ctx, *, message):
    for guild in client.guilds:
        for member in guild.members:
            await member.send(message)

    await ctx.send("Messages sent!")

"""
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))
"""

LinuxBoi().run(linuxboi_token)
# client.run(read_token(), bot=False)
