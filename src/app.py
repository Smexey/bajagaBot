from discord import Intents
import os
from discord.ext import commands
from bajaga import Bajaga


def main():
    TOKEN = os.environ.get('DISCORD_API_TOKEN')
    PREFIX = '!'

    intents = Intents.default()
    intents.members = True


    bot = Bajaga(command_prefix=PREFIX)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
