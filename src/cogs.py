import discord
from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from discord import VoiceClient, VoiceChannel
import discord.ext.commands
import const

class Radio(discord.ext.commands.Cog, name='Greetings module'):
   
    def __init__(self, bot):
        self.bot: Bot = bot
        self.player: VoiceClient = None

    async def play_url(self, ctx: Context, url: str) -> None:
        channel: VoiceChannel = ctx.message.author.voice.channel
        voice_client: VoiceClient = discord.utils.get(
            self.bot.voice_clients, guild=ctx.guild)
        try:
            if voice_client:
                self.player.stop()
            else:
                self.player = await channel.connect()
        except NameError:
            self.player = await channel.connect()
            
        self.player.play(FFmpegPCMAudio(url))
        await ctx.send(f'Tvoje usi cuju: {url}')
        await ctx.send(self.bot.get_emoji(const.Emojis.DOGE_DANCE))

    @discord.ext.commands.command(aliases=['r'], name="Play radio")
    async def radio(self, ctx: Context, url: str = const.Radio.ROCK):
        await self.play_url(ctx, url)

    @discord.ext.commands.command(aliases=['n'], name="Naxi radio")
    async def naxi(self, ctx: Context, subtype: str = ""):
        # TODO: add more naxis
        url = const.Radio.NAXI
        await self.play_url(ctx, url)

    @discord.ext.commands.command(aliases=['s'], name="Stop player")
    async def stop(self, ctx: Context):
        if self.player is not None:
            self.player.stop()
            await ctx.send(self.bot.get_emoji(const.Emojis.BONK))
