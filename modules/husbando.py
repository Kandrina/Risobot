import random
import json
import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Husbando(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def husbando(self, ctx):
        img_list = os.listdir('./images/')
        print(img_list())

        # Counts the maps to be used in a randint
        image_count = len(img_list) - 1

        await ctx.send(file=discord.File(img_list[random.randint(0, image_count)]))

def setup(bot):
    bot.add_cog(Husbando(bot))
