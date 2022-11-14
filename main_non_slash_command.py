import nextcord
import re
from selenium import webdriver

from nextcord.ext import commands, tasks




intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

with open('token.txt', 'r') as f:
    contents = f.read()

bot = commands.Bot(command_prefix="w", description=None, intents=intents)

@bot.command()
async def test(ctx,message):
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

# this is the commnand to search for related things in arknighs

@bot.event
async def on_command_error(ctx,error):
    await ctx.send(error)

@bot.event
async def repeat(ctx,word):
    await ctx.send(word)




        
        
                

    return
    
bot.run(contents)