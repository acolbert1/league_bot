import os
import random
import cassiopeia as cass
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
api_key = os.getenv('RIOT_API_KEY')

cass.set_riot_api_key(api_key)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.command(name="rank")
async def account_level(ctx, playername):
    if ctx.author == bot.user:
        return
  
    summoner = cass.get_summoner(name=playername)
    response = ("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name, level=summoner.level, region=summoner.region))
    await ctx.send(response)

bot.run(token)