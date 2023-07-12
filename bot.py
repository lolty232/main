import os

import disnake
from disnake.ext import commands
import config
from config import *

client = commands.Bot(command_prefix='!dsafdsfdfdsf', intents=disnake.Intents.all())
client.remove_command('help')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
