import random
import json
import glob

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Shuu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shuu(self, ctx):
        for image in glob.glob('../images/'):
            print(image)

        await ctx.send(file=discord.File('image'))

def setup(bot):
    bot.add_cog(Shuu(bot))
