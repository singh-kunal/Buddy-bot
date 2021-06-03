import os
import discord
import requests
import json
import random
from keep_alive import keep_alive
#from replit import db



"https://animechan.vercel.app/guide"

client = discord.Client()


def get_quote():
  response = requests.get("https://animechan.vercel.app/api/random")
  json_data = json.loads(response.text)
  quote = '"' + json_data['quote'] + '"' + "\n ~ " + '_' + json_data['character'] + '_' + "\n from " + json_data['anime']
  return(quote)

def specific_quote(anime):
  response = requests.get('https://animechan.vercel.app/api/quotes/anime?title=' + anime)
  json_data = json.loads(response.text)
  index = random.randint(0,len(json_data)-1)
  temp = json_data[index]
  quote = '**' + temp['anime'] + '**' + "\n" + '"' + temp['quote'] + '"' + "\n ~ " + '_' + temp['character'] + '_'
  
  return(quote)



@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #if message.content.startswith("bud help"):
    #await message.channel.send("")

  if message.content.startswith("hello"):
    await message.channel.send("Hey Buddy! 🙂")
  
  if message.content.startswith("noob"):
    await message.channel.send(message.author.mention)
    await message.channel.send("git gud! 🙂")

  if message.content.startswith("bud quote"):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith("bud squote"):
    anime = message.content.split("bud squote ",1)[1]
    quote = specific_quote(anime)
    print(anime)
    #await message.channel.send("Enter Anime name")
    #squote = await client.wait_for("message", timeout=60)
    #print(squote)
    
    #if squote.author == message.author:
      #quote = specific_quote(squote)
    await message.channel.send(quote)
    
keep_alive()
client.run(os.getenv("TOKEN"))
