import discord
from discord.ext import commands
import datetime 
import nextcord
from nextcord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user}")

@bot.event
async def on_message(message):
    if message.author.id == 353175624283717643: 
        await message.channel.send("😐")
        if "😐" in message.content:
            await message.author.edit(timeout=datetime.datetime.utcnow() + datetime.timedelta(seconds=60))

bot.run("token")  
