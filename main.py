import nextcord
from nextcord.ext import commands
import aiohttp
import bs4



intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix="w", description=None, intents=intents)

@bot.command()
async def test(ctx,message):
    await ctx.send(message)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

# this is the commnand to search for related things in arknighs

@bot.command()
async def arknights(ctx,arknights):
    arknights = "null"
    return
    
bot.run("MTAxODAzNjA3MzI1Njk5Njg3Ng.G8Kf5k.irE21heU8pEnoCvCmArqwvounQoDZdjfTpVFfM")

