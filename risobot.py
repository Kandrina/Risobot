# Just a shitty test
# The way to type a version:
# {full release}.{new features}.{fixes}-{DD/MM}A/B/F (Alpha, Beta, Final)
# Example: 0.1.0-0110A (1st of October, Alpha)
import glob
import os
import json

from discord.ext import commands

# Init the bot, prefix and help description.
bot = commands.Bot(command_prefix='!', description='Commands currently available')


@bot.event
async def on_ready():
    # Prints the bot name, discrim and ID when started up
    print('METALLICA!')
    print(f'------\nReady!\n{bot.user}\n{bot.user.id}\n------')
    

# Searches for existing modules (commands) in /modules/
if __name__ == '__main__':
    for module in glob.glob('./modules/*.py'):
        print(module)
        try:
            bot.load_extension(f'modules.{os.path.basename(module)[:-3]}')
        except Exception as e:
            exc = f'{__name__}: {e}'
            print(f'Failed to load module {module}\n{exc}')

# Opens the json file and fetches the token
with open('risobot.json') as f:
    diepy = json.load(f)
    token = diepy.get('token')
bot.run(token)
