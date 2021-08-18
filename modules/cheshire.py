import random
import json

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Cheshire(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cheshire(self, ctx):

        with open('json/cheshire.json') as f:
            data = json.load(f)
        #print(data)
        quotes = data["quotes"]

        # Counts the maps to be used in a randint
        quotes_count = len(quotes) - 1

        embedVar = discord.Embed(title="", description="", color=0x009898)
        embedVar.add_field(name="Cheshire", value=quotes[random.randint(0, quotes_count)], inline=False)
        embedVar.set_thumbnail(url="https://banner2.cleanpng.com/20180616/hxa/kisspng-traffic-sign-roadworks-warning-sign-denmark-5b2569ae9b5ec0.3560216115291785426364.jpg")
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Cheshire(bot))
