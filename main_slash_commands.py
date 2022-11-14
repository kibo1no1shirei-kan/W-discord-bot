import nextcord
import re
from nextcord.ext import commands, tasks
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import Chrome



intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

with open('token.txt', 'r') as f:
    contents = f.read()

bot = commands.Bot(command_prefix="w", description=None, intents=intents)

@bot.slash_command()
async def test(ctx,message):
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.event
async def on_command_error(ctx,error):
    await ctx.send(error)

@bot.event
async def repeat(ctx,word):
    await ctx.send(word)



@bot.slash_command()
async def arknights(ctx,operator):
    pass






bot.run(contents)