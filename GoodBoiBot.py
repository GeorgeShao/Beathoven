from discord.ext.commands import Bot

BOT_PREFIX = "~"
file = open("TOKEN.txt","r")
TOKEN = file.read()

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_message(message):
    #Prevents bot from responding to other bots, including itself.
    if message.author.bot:
        return
    await client.process_commands(message)

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("pong")

@client.command(pass_context=True)
async def square(ctx, number: int):
    answer = number ** 2
    await client.say(f"{number} squared is {answer}")

client.run(TOKEN)
