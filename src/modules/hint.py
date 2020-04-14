import random

from discord.ext import commands


class Hint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hint(self, ctx):

        # Hints for the game
        hints = [
            'If you ever encounter `Talis`, a wise choice would be to abandon the fight.',
            '`Yellow-Eyes (Damien Moon)` was once a character of great importance, before the incident.',
            'Not even diamonds compare in structural strength of plasteel.',
            '`Night Blue` can sometimes help you out, but only if the situation is in his interest or gain.',
            'Plasteel is an ancient metal alloy forgotten with time.',
            '`Talis` is the only person who has managed to severely injure `Yellow-Eyes` without the need of silver.',
            'The dominating currency is coins named `flakes`!',
            'Other-Worlders souls are made up differently, and cannot be detected by magic in Nova Regna.',
            'Nordania is the oldest empire, and hosts the council and emperor of every era.',
            '`Damien` seemingly have a curse that will either benefit him.... Or not.',
            'The Secret Order of Fallen Angels have been around since the beginning of times.',
            'Tales, legends and books say that direwolves were viscious creatures, but lacks the ability to transform.... Unlike `Yellow-Eyes`.',
            'CREEPER!',
            'AW MAN!',
            'Super luck? I wonder who...',
            'It is advised to not pull on someone\'s tail or ears.',
            '`Melie` is an idiot, but `Yellow-Eyes` is far more irritating.'
        ]

        # Counts the hints to be used in a randint
        hints_count = len(hints) - 1

        await ctx.send(hints[random.randint(0, hints_count)])


def setup(bot):
    bot.add_cog(Hint(bot))
