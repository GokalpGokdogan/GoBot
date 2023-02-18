import discord
from discord.ext import commands
import os
import random
#import asyncio
from replit import db
import giphy_client
from giphy_client.rest import ApiException

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents = intents, command_prefix='g!')


@client.event
async def on_ready():
  print("Lets gooooo baby!!")
  names_list = []
  
  with open('Rizzionary.txt', 'r') as _:
      for line in _:
          line = line.strip()
          if line:
            if not line in db["rizzionary"]:
              #print("Exists...")
            #else:
              names_list.append(line)
            else:
              return
  print(names_list)
  
  db["rizzionary"]=names_list
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  message_up = message.content.lower()
  message.content = message_up
  messageList = message_up.split()
  
  if "rizz" in messageList:
    ans = " "
    if db["rizzionary"]:
      ans = "Rizz Lord: "+ random.choice(db["rizzionary"]) + ". "
    else:
      ans = "W Rizz... "

    embed=discord.Embed(title=ans, color=0x3875d6)
    embed.set_thumbnail(url="https://assets1.ignimgs.com/2019/09/19/pipe-1568931609207_160w.jpg?width=1280")
    embed.set_author(name="GoBot", url="https://www.linkedin.com/in/g%C3%B6kalp-g%C3%B6kdo%C4%9Fan-037103231/")
    #embed.add_field(name=ans, value=" ", inline=False)
    await message.send(embed=embed)

      
  if message_up.startswith('g!updateRizz'):
    message_new = message_up.split(' ', 1)[1]
    
    updateRizz(message_new)
    
  if message_up.startswith('g!test'):
    
    message_new = message_up.split(' ', 1)[1]
  await client.process_commands(message)





  
### In current implementation it doesnt delete items, just adds them
def updateRizz(str,message):
  if "rizzionary" in db.keys():
    newRizzionary = db["rizzionary"]

    if str in newRizzionary:
      
      print("Deleted: " + str)
      newRizzionary.remove(str)
    else:
      newRizzionary.append(str)
      
      print("Added: " + str)
    db["rizzionary"] = newRizzionary
  else:
    
    print("Added: " + str)
    db["rizzionary"] = [str]

@client.command()
async def hi(ctx):
  ans = f"How you doin?! {ctx.author.name}"

  embed=discord.Embed(title=ans, color=0x3875d6)
  embed.set_thumbnail(url="https://assets1.ignimgs.com/2019/09/19/pipe-1568931609207_160w.jpg?width=1280")
  embed.set_author(name="GoBot", url="https://www.linkedin.com/in/g%C3%B6kalp-g%C3%B6kdo%C4%9Fan-037103231/")
  
  #embed.add_field(name=ans, value=" ", inline=False)
  await ctx.send(embed=embed)



  
@client.command()
async def gif(ctx, q="Slap"):
  
  api_key = os.environ["Giphy_Key"]
  giphy=giphy_client.DefaultApi()

  try:
    response = giphy.gifs_search_get(api_key, q, limit=25, rating='r')
    lst = list(response.data)
    giff = random.choice(lst)

    emb = discord.Embed(title = q, color=0x3875d6)
    emb.set_author(name="GoBot", url="https://www.linkedin.com/in/g%C3%B6kalp-g%C3%B6kdo%C4%9Fan-037103231/")
    emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

    await ctx.channel.send(embed = emb)

  except ApiException as e:
    await ctx.channel.send("You can't even search right. Noob...")

@client.command()
async def slap(ctx,  u= None):
  
  if not u or str(ctx.author.id) == str(u.strip('@<>')) :
    await ctx.channel.send(f'{ctx.author.name} slapped himself/herself. What an idiot.')
  else:
    await ctx.channel.send(f'{ctx.author.name} slapped {u}. LOL.')

  
  await gif(ctx, 'slap')


@client.command()
async def coin(ctx, msg):
  '''
  await ctx.channel.send("Coin is tossed:\n")
  for i in range(1,4):
    await ctx.channel.send(str(i) + i*"."+"\n")
    await asyncio.sleep(0.5)
  '''  

  coin = random.randrange(0,2)

  ans=''  
  if coin == 0:
    ans = "Result is Heads.\n"
    if msg.startswith('heads'):
      ans += "You won.\n"
    else:
      ans += "You lost.\n"

  else:
    ans = "Result is Tails.\n"
    if msg.startswith('tails'):
      ans += "You won.\n"
    else:
      ans += "You lost.\n"
  ans += f"{ctx.author.name}"
  embed=discord.Embed(title="Coin Toss", color=0x3875d6)
  embed.set_thumbnail(url="https://assets1.ignimgs.com/2019/09/19/pipe-1568931609207_160w.jpg?width=1280")
  embed.set_author(name="GoBot", url="https://www.linkedin.com/in/g%C3%B6kalp-g%C3%B6kdo%C4%9Fan-037103231/")
  embed.add_field(name="1.", value=" ", inline=False)
  embed.add_field(name="2..", value=" ", inline=False)
  embed.add_field(name="3...", value=" ", inline=True)
  embed.add_field(name=ans, value=" ", inline=False)
  await ctx.send(embed=embed)


@client.command()
async def dice(ctx, msg):
  '''
  await ctx.channel.send("Dice is tossed:\n")
  for i in range(1,4):
    await ctx.channel.send(str(i) + i*"."+"\n")
    await asyncio.sleep(0.5)
  '''  
    
  dice = random.randrange(1,7)

  ans = ' '
  if dice == int(msg):
    ans = f"You won, {ctx.author.name}. It was " + str(dice) +".\n"
  else:
    ans = f"You lost, {ctx.author.name}. It was " + str(dice) +".\n"


  embed=discord.Embed(title="Dice Throw", color=0x3875d6)
  embed.set_thumbnail(url="https://assets1.ignimgs.com/2019/09/19/pipe-1568931609207_160w.jpg?width=1280")
  embed.set_author(name="GoBot", url="https://www.linkedin.com/in/g%C3%B6kalp-g%C3%B6kdo%C4%9Fan-037103231/")
  embed.add_field(name="1.", value=" ", inline=False)
  embed.add_field(name="2..", value=" ", inline=False)
  embed.add_field(name="3...", value=" ", inline=True)
  embed.add_field(name=ans, value=" ", inline=False)
  await ctx.send(embed=embed)

client.run(os.environ['TOKEN'])
