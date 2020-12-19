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
        if "hi" in message.content.lower() or "hello" in message.content.lower():
            if "child" not in message.content.lower() and "high" not in message.content.lower() and "this" not in message.content.lower() and "thing" not in message.content.lower() and "his" not in message.content.lower():
                num = random.randint(1, 10)
                if num == 1:
                    await message.channel.send("fuck you " + str(message.author) + "!")
                else:
                    await message.channel.send("hi " + str(message.author) + "!")
        if "long" in message.content.lower() and "along" in message.content.lower():
            await message.add_reaction("🍆")
            await message.channel.send("still not as long as my ******")
        if "fuck" in message.content.lower() or "shit" in message.content.lower():
            await message.add_reaction("✝")
            await message.add_reaction("⛪")
            await message.channel.send("Please stop swearing senpai!")
        if "god" in message.content or "lord" in message.content:
            await message.channel.send("Remember to capitalize the Lord's name!")
            await message.add_reaction("✝")
            await message.add_reaction("⛪")
        if "oh my god" in message.content.lower() or "oh my lord" in message.content.lower():
            await message.channel.send("Don't use the Lord's name in vain!")
            await message.add_reaction("✝")
            await message.add_reaction("⛪")
        if "cri" in message.content.lower() or "cry" in message.content.lower():
            await message.add_reaction("✝")
            await message.add_reaction("⛪")
            await message.channel.send("awwww, are you okay? it's okay not to be okay")
        if "joe" in message.content.lower() in message.content.lower():
            await message.channel.send("JOE MAMA")
    
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
async def hug(ctx):
    msg = str(ctx.message.content).lower()
    print(msg)
    full_msg = f"""
**Interac:tm: Hug-Transfer** (but with social distancing 6ft apart)
Sender: <@!{ctx.message.author.id}>
Recipient: {ctx.message.content[ctx.message.content.index("<"):ctx.message.content.index(">")+1]}
Message: {ctx.message.content[ctx.message.content.index(">")+2:]}
---
*This individual has AutoDeposit enabled, so all hug transfers are automatically accepted and deposited into their hug chequing account.*
"""
    await ctx.channel.send(full_msg)
    print("Sent hug to " + str(ctx.channel))

@client.command()
async def coin(ctx):
    num = random.randint(1, 2)
    if num == 1:
        msg = "heads"
    else:
        msg = "tails"
    await ctx.channel.send(msg)
    print(f"Sent message to \"{msg}\" {str(ctx.channel)}")

client.run(TOKEN)