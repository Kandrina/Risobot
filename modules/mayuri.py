import random
import json

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Mayuri(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mayuri(self, ctx):

        with open('json/mayuri.json') as f:
            data = json.load(f)
        #print(data)
        quotes = data["quotes"]
        name = data["name"]
        image = data["image"]
        color = int(data["color"],16)

        # Counts the maps to be used in a randint
        quotes_count = len(quotes) - 1

        embedVar = discord.Embed(title="", description="", color=color)
        embedVar.add_field(name=name, value=quotes[random.randint(0, quotes_count)], inline=False)
        embedVar.set_thumbnail(url=image)
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Mayuri(bot))
