import os
import random

import discord
from discord.ext import commands

# @bot.command()
# async def check_server(ctx):
#     # Get the server object
#     server = ctx.guild
    
#     if server:
#         await ctx.send(f"This command was published in: **{server.name}** (ID: {server.id})")
#     else:
#         await ctx.send("This command was sent in a Private Message (DM).")

class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.images_path = bot.images_path

    @commands.command(name="kobe")
    async def kobe(self, ctx:commands.Context):
        server = ctx.guild
        prefix = ""
        if server:
            server_str = server.name + '_' + str(server.id)
            prefix = os.path.join(self.images_path, server_str)
        else:
            await ctx.send("This command was sent in a Private Message (DM).\nNot Support Kobe")
            return       

        kobe_dir = os.path.join(prefix, "kobe")
        os.makedirs(kobe_dir, exist_ok=True)

        files_name = os.listdir(kobe_dir)

        if len(files_name) == 0:
            await ctx.send("No image in Database.")
            return
        ind = random.randint(0, len(files_name)-1)
        
        image_path = os.path.join(kobe_dir, files_name[ind])
        
        await ctx.send(f"{ctx.author.mention}孩子們。這不好笑", file=discord.File(image_path))

async def setup(bot):
    await bot.add_cog(Image(bot))

