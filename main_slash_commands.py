import nextcord
import re
import asyncio
from nextcord.ext import commands, tasks
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import bs4
from bs4 import BeautifulSoup


intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="w", description=None, intents=intents)

@bot.slash_command()
async def test(interaction,message):
    await interaction.send(message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_command_error(interaction,error):
    await interaction.send(error)

@bot.event
async def repeat(interaction,word):
    await interaction.send(word)

@bot.slash_command()
async def arknights(interaction,operator):
    await interaction.response.defer()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    options.page_load_strategy = 'normal'
    driver.get(f"https://aceship.github.io/AN-EN-Tags/akhrchars.html?opname={operator}&story=0")
    await asyncio.sleep(15)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    operator_quotes = soup.find_all("td")
    gender = driver.find_element(By.ID, "op-gender").text
    chara_image_elements = driver.find_element(By.CLASS_NAME, "chara-image").get_attribute("src")
    operator_quotest = operator_quotes[1].text
    author = interaction.user
    authoravatar = author.display_avatar.url
    embed=nextcord.Embed(title=operator, url=f"https://aceship.github.io/AN-EN-Tags/akhrchars.html?opname={operator}", description=operator_quotest , color=0x0923e1)
    embed.set_author(name=author, icon_url=authoravatar)
    embed.add_field(name="Sex", value=gender, inline=True) #basic file
    #embed.add_field(name="Combat Experience", value=exp, incline=False)

    embed.set_author(name=author, icon_url=authoravatar) 
    embed.set_image(url=chara_image_elements)
    await interaction.followup.send(embed=embed)
    driver.quit()
