import random
import json

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx):

        with open('json/ban.json') as f:
            data = json.load(f)
        #print(data)
        quotes = data["quotes"]
        images = data["images"]

        # Counts the maps to be used in a randint
        quotes_count = len(quotes) - 1
        images_count = len(images) - 1

        embedVar = discord.Embed(title="", description="", color=0x408DD2)
        embedVar.add_field(name="Ban", value=quotes[random.randint(0, quotes_count)], inline=False)
        embedVar.set_thumbnail(url=images[random.randint(0, images_count)])
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Ban(bot))
