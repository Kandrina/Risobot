import random
import json

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, first, second):
        firstfile = 'json/'+first+'.json'
        print(firstfile)
        with open(firstfile) as ff:
            firstdata = json.load(ff)
        firstquotes = firstdata["quotes"]
        firstname = firstdata["name"]
        firstcolor = int(firstdata["color"],16)
        firstimage = firstdata["image"]

        secondfile = 'json/'+second+'.json'
        print(secondfile)
        with open(secondfile) as sf:
            seconddata = json.load(sf)
        secondquotes = seconddata["quotes"]
        secondname = seconddata["name"]
        secondcolor = int(seconddata["color"],16)
        secondimage = seconddata["image"]

        # Counts the maps to be used in a randint
        firstquotes_count = len(firstquotes) - 1
        secondquotes_count = len(secondquotes) - 1

        firstembedVar = discord.Embed(title="", description="", color=firstcolor)
        firstembedVar.add_field(name=firstname, value=firstquotes[random.randint(0, firstquotes_count)], inline=False)
        firstembedVar.set_thumbnail(url=firstimage)
        
        secondembedVar = discord.Embed(title="", description="", color=secondcolor)
        secondembedVar.add_field(name=secondname, value=secondquotes[random.randint(0, secondquotes_count)], inline=False)
        secondembedVar.set_thumbnail(url=secondimage)
        
        await ctx.send(embed=firstembedVar)
        await ctx.send(embed=secondembedVar)

def setup(bot):
    bot.add_cog(Chat(bot))
