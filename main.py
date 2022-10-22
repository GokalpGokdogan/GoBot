import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Lets gooooo baby!!")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  message_up = message
  if message_up.content.startswith('G') or message_up.content.startswith('D'):
    await message.channel.send("How you doin?!")


client.run(os.environ['TOKEN'])
