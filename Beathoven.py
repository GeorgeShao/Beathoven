from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import discord
import random

BOT_PREFIX = "~"
file = open("TOKEN.txt","r")
TOKEN = file.read()

client = commands.Bot(command_prefix = BOT_PREFIX)

# Confirms that bot is connected to server
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)

@client.event
async def on_message(message):
    print(message.author, message.content)
    if message.author != client.user:
        if "hi" in message.content or "hello" in message.content:
            await message.channel.send("hi " + str(message.author) + "!")
    
    # Checks if message is a command
    await client.process_commands(message)

    # Prevents bot from responding to other bots
    if message.author == client.user:
        return

@client.command()
async def dice(ctx):
    num = random.randint(1, 6)
    await ctx.channel.send(num)
    print("Sent message \"" + str(num) + "\" to #" + str(ctx.channel))

@client.command()
async def ping(ctx):
    await ctx.channel.send("pong")
    print("Sent message \"pong\" to #" + str(ctx.channel))

@client.command()
async def name(ctx):
    await ctx.channel.send("pong")
    print("Sent message \"pong\" to #" + str(ctx.channel))

client.run(TOKEN)