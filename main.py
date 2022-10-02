import nextcord
from nextcord.ext import commands
import aiohttp
import bs4

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")




# this is the commnand to search for related things in arknighs

@bot.command()
async def arknights(ctx,arknights):
    pass
    
