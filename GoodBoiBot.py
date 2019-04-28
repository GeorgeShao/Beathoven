from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
import discord

BOT_PREFIX = "~"
file = open("TOKEN.txt","r")
TOKEN = file.read()

client = commands.Bot(command_prefix = '.')

#Confirms that bot is connected to server
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with fellow humans"))
    print("Logged in as " + client.user.name)
    servers = list(client.servers)
    print("Connected on " + str(len(client.servers)) + " servers:")
    for x in range(len(servers)):
        print('    ' + servers[x-1].name)

@client.event
async def on_message(message):
    #Checks if message is a command
    await client.process_commands(message)

    #Prevents bot from responding to other bots
    if message.author == client.user:
        return

    channel = message.channel
    username = message.author.name
    time = str(message.timestamp)

@client.command(name="ping", description="Ping Pong", pass_context=True)
async def ping(ctx):
    print(ctx.message.author.name + " has triggered ping command at " + str(ctx.message.timestamp))
    await client.say('Pong!')

client.run(TOKEN)