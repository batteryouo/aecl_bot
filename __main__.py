
import datetime
import os
from pathlib import Path
import random

import discord
from discord.ext import commands, tasks

import asyncio

from aecl_bot import utils

AUTO_LEAVE_TIME = 60
auto_leave_tasks = {} 

class AECL_Bot(commands.Bot):
    def __init__(self, img_path):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=">", intents=intents)

        self.images_path = img_path

    async def setup_hook(self):
        cog_dir = os.path.join("aecl_bot\\cog")
        for filename in os.listdir(cog_dir):
            file_path = os.path.join(cog_dir, filename)
            file_path = file_path.replace("\\", '.')
            if file_path.endswith(".py") and not file_path.endswith("__init__.py"):
                await self.load_extension(f"{file_path[:-3]}")


current_file = Path(__file__).resolve()
base_dir = current_file.parent
image_dir = os.path.join(base_dir, "image")
bot = AECL_Bot(img_path=image_dir)

@bot.event
async def on_ready():
    print(f'user: {bot.user}')

def main(token):
    bot.run(token=token)

if __name__ == "__main__":
    token = utils.read_file.read_token("DISCORD_BOT_TOKEN.txt")
    main(token=token)

# sounds_path = os.path.join(os.curdir, "sounds")
# images_path = os.path.join(os.curdir, "images")


# @bot.event
# async def on_ready(ctx):
#     print(f'Logged in as {ctx.user.name}')
