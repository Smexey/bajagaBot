import discord
from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from discord import VoiceClient, VoiceChannel
import discord.ext.commands
import const
from discord.ext import commands



class Radio(discord.ext.commands.Cog, name='Radio module'):

    def __init__(self, bot):
        self.bot: Bot = bot
        self.player: VoiceClient = None

    async def play_url(self, ctx: Context, url: str) -> None:
        msg: discord.Message = ctx.message
        channel: VoiceChannel = msg.author.voice.channel

        # Bot cant join more than 1 voice channel per server(guild)
        voice_client: VoiceClient = discord.utils.get(
            self.bot.voice_clients, guild=ctx.guild)
        if voice_client:
            self.player.stop()
        else:
            self.player = await channel.connect()

        self.player.play(FFmpegPCMAudio(url))
        await ctx.send(f'Tvoje usi cuju: {url}')
        await msg.add_reaction(self.bot.get_emoji(const.Emojis.DOGE_DANCE))

    @commands.command(aliases=['r'], name="Play radio")
    async def radio(self, ctx: Context, url: str = const.Radio.ROCK):
        await self.play_url(ctx, url)

    @commands.command(aliases=['n'], name="Naxi radio")
    async def naxi(self, ctx: Context, subtype: str = ""):
        # TODO: add more naxis
        url = const.Radio.NAXI
        await self.play_url(ctx, url)

    @commands.command(aliases=['s'], name="Stop player")
    async def stop(self, ctx: Context):
        if self.player.is_playing():
            self.player.stop()
            msg: discord.Message = ctx.message
            await msg.add_reaction(self.bot.get_emoji(const.Emojis.BONK))

    @commands.command(name='leave', aliases=['disconnect'])
    @commands.has_permissions(manage_guild=True)
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]
