import random
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os

TOKEN = os.environ.get('DISCORD_API_TOKEN')
PREFIX = '!'
print(TOKEN)
bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print('Music Bot Ready')


@bot.command(aliases=['p', 'pla'])
async def play(ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
    global player
    channel = ctx.message.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
        if voice_client:
            player.stop()
        else:
            player = await channel.connect()
    except NameError:
        player = await channel.connect()
    player.play(FFmpegPCMAudio('http://stream.radioparadise.com/rock-128'))


@bot.command(aliases=['n'])
async def naxi(ctx, url: str = 'naxi'):
    global player
    channel = ctx.message.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
        if voice_client:
            player.stop()
        else:
            player = await channel.connect()
    except NameError:
        player = await channel.connect()
    player.play(FFmpegPCMAudio('https://naxi64ssl.streaming.rs:9162/;stream'))


@bot.command(aliases=['s', 'sto'])
async def stop(ctx):
    player.stop()

bot.run(TOKEN)
