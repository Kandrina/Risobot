import os

import discord
from discord.ext import commands
import json


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        with open('./diepy.json') as f:
            diepy = json.load(f)
            name = diepy.get('name')
            version = diepy.get('version')
            codename = diepy.get('codename')
            author = diepy.get('author')
            description = diepy.get('description')

        # The embed
        embed = discord.Embed(description='**--Information--**')
        embed.add_field(name='**Name:**', value=name, inline=False)
        embed.add_field(name='Description:', value=description, inline=False)
        embed.add_field(name='**Version:**', value=version, inline=False)
        embed.add_field(name='**Codename:**', value=codename, inline=False)
        embed.add_field(name='**Author(s):**', value=author, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
