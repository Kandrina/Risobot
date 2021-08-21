import random
import json
import glob

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Husbando(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def husbando(self, ctx):
        for image in glob.glob('./images/'):
            print('Image: ' +image)

        await ctx.send(file=discord.File(image))

def setup(bot):
    bot.add_cog(Husbando(bot))
