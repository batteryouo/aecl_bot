import discord
from discord.ext import commands

class Talking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Mamba(self, ctx):
        await ctx.send("Man! What can I say.\nMamba Out!")

async def setup(bot):
    await bot.add_cog(Talking(bot))