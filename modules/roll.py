import discord
from discord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def roll(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please enter a valid dice to roll.\nValid dices:\nd6, d12, d20, d100')

    @roll.command()
    async def d6(self, ctx):
        number = random.randint(1, 6)
        await ctx.send(f'You rolled `{number}`!')

    @roll.command()
    async def d12(self, ctx):
        number = random.randint(1, 12)
        await ctx.send(f'You rolled `{number}`!')

    @roll.command()
    async def d20(self, ctx):
        number = random.randint(1, 20)
        await ctx.send(f'You rolled `{number}`!')

    @roll.command()
    async def d100(self, ctx):
        number = random.randint(1, 100)
        await ctx.send(f'You rolled `{number}`!')

    @roll.command()
    async def talis(self, ctx):
        await ctx.send('Talis rolled `9999` for Damien!')


def setup(bot):
    bot.add_cog(Roll(bot))
