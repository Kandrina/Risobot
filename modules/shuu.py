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
        quotes = data["quotes"]

        # Counts the maps to be used in a randint
        quotes_count = len(quotes) - 1

        embedVar = discord.Embed(title="", description="", color=0x9303A7)
        embedVar.add_field(name="Shuu Tsukiyama", value=quotes[random.randint(0, quotes_count)], inline=False)
        embedVar.set_thumbnail(url="https://cdn.anisearch.de/images/character/cover/full/45/45986.webp")
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Shuu(bot))
