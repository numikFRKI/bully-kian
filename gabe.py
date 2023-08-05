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
    if "kids" in message.content:
        await message.ctx.reply("where 🤤")

bot.run("token")  # Replace with your actual bot token
