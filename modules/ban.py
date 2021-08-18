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

        # Counts the maps to be used in a randint
        quotes_count = len(quotes) - 1

        embedVar = discord.Embed(title="", description="", color=0x408DD2)
        embedVar.add_field(name="Ban", value=quotes[random.randint(0, quotes_count)], inline=False)
        embedVar.set_thumbnail(url="https://i.pinimg.com/736x/8a/99/c2/8a99c255ffe51609b2b0f096125c9542--seven-deadly-sins-cinnamon-roll.jpg")
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Ban(bot))
