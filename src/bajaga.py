
from discord.ext import commands

class Bajaga(commands.Bot):

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        print(f'{self.emojis}')
