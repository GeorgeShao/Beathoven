from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import discord

BOT_PREFIX = "~"
file = open("TOKEN.txt","r")
TOKEN = file.read()

client = commands.Bot(command_prefix = BOT_PREFIX)

#Confirms that bot is connected to server
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)

@client.event
async def on_message(message):
    #Checks if message is a command
    await client.process_commands(message)

    #Prevents bot from responding to other bots
    if message.author == client.user:
        return

@client.command
async def test(author, message):
    await message.channel.send('I heard you! {0.name}'.format(author))

@client.command()
async def ping(ctx):
    # await client.say('Pong!')
    await ctx.send("gay")
    # await client.send_message(ctx.channel, "^ gay")

client.run(TOKEN)