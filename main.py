import discord
from discord.ext import commands
import music

# cogs = [music]

# intents = discord.Intents.all()  #default() intents.message_content = True
# client = commands.Bot(command_prefix='g!', intents=intents)

# for i in range(len(cogs)):
#    cogs[i].setup(client)


intents = discord.Intents.all()
client = commands.Bot(command_prefix='g!', intents=intents, case_insensitive=True)

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)
# client.load_extension(f"music")

@client.event
async def on_ready():
    print(f'Bot connected ')


# @client.event
# async def on_ready():
# print("Lets gooooo baby!!")

client.run("MTAzMzQ3OTU1MzA4OTI4NjE3NA.GoX25D.5Z8oI0abMmmo-HIwB-oYCm6X_gSaPV1UdXm3-E")
