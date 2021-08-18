import random
import json

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Shuu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shuu(self, ctx):

        with open('json/shuu.json') as f:
            data = json.load(f)
        #print(data)
        quotes = data["quotes"]
        images = data["images"]

        # Counts the maps to be used in a randint
        quotes_count = len(quotes) - 1
        images_count = len(images) - 1

        embedVar = discord.Embed(title="", description="", color=0x9303A7)
        embedVar.add_field(name="Shuu Tsukiyama", value=quotes[random.randint(0, quotes_count)], inline=False)
        embedVar.set_thumbnail(url=images[random.randint(0, images_count)])
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Shuu(bot))
