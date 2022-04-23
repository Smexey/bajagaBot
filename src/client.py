from discord import Intents
import os
from cogs import *
from bajaga import Bajaga


def main():
    TOKEN = os.environ.get('DISCORD_API_TOKEN')
    PREFIX = '!'

    intents = Intents.default()
    intents.members = True

    bot = Bajaga(command_prefix=PREFIX)
    bot.add_cog(Radio(bot=bot))

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
