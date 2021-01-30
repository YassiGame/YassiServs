# bot.py
import os
import random
import discord
import platform
import typing
import datetime
import re

from urllib import parse, request
from discord.ext import commands
from discord.ext.commands import Bot

Prefix = ('f!')
bot = commands.Bot(command_prefix=(Prefix))

#au démarage
@bot.event
async def on_ready():
    # Setting `Playing ` status
    await bot.change_presence(activity=discord.Streaming(name=Prefix + 'help' , url="http://www.twitch.tv/0"))

    print("Bot is ready!")


#test-commande
@bot.command(name='test')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    Response = random.choice(brooklyn_99_quotes)
    await ctx.send(Response)

# 2eme commande
@bot.command(name='Yassi' + 'yassi' + 'ㄚ卂丂丂丨')
async def nine_nine(ctx):
    Yassi = '**Yassi est un BG**'

    response = (Yassi)
    await ctx.send(response)

#3 invite troll
@bot.command(name='invite')
async def nine_nine(ctx):
    Invite = "**C'est un bot privée ta cru que tu vas avoir le lien d'invite X)**"

    await ctx.send(Invite)


#4 commande say
@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

#5
@bot.command()
async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]):
    await ctx.send(what)

#6
@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))
@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')

#7 ban
@bot.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    """Mass bans members with an optional delete_days parameter"""
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await ctx.send('The member(s) as baned')
@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')


#9 bg commande
@bot.command()
async def bg(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got **BG** for {}'.format(slapped, reason))

#ping pong X)
@bot.command()
async def ping(ctx):
    '''
    My ping pong ;)
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

#echo (say)
    '''
    Another say command
    '''
@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)



bot.run("ODAzOTk1NTg3MjI0OTI4MzIz.YBF5PQ.hnWmo5neszR0mf79ymMFbV_QK1A")