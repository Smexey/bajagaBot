from radio import Radio
from discord.ext import commands

from discord import Game
from music import Music

class Bajaga(commands.Bot):

    def __init__(self, command_prefix, description=None, **options):
        activity = Game(name='muziku na struju ⚡')
        super().__init__(command_prefix,
                         description, activity=activity, **options)
        self.add_cog(Radio(bot=self))
        # self.add_cog(Music(bot=self))


    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
