# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print('{} has connected to Discord!'.format(client.user))

  if message.content == 'hello!':
    await message.channel.send('Hi, I am the MORSpineBot :robot:! I was created to answer any and all general questions you may have :grin:. For a list of command options that I currently recognize, simply type "options!"')

  elif message.content == 'options!':
    await message.channel.send('The following is a list of commands that I currently recognize... Be sure to enter an exclamation after each command, e.g. login! \n1. help! \n2. zaki! \n3. login! \n4. papersandtextbooks! \n5. instructionsandmeasurements! \n6. tables! \n7. otherquestion!')

# First command
  elif message.content == 'help!':
    await message.channel.send('MORSpineBot at your service! Type "options!" for a list of commands that I currently recognize!')

# Second command
  elif message.content == 'zaki!':
    await message.channel.send('Can your question be answered by someone else? \n yes! \n no!')
  elif message.content == 'yes!':
    await message.channel.send('Feel free to reach out to any of the Team Leads.')
  elif message.content == 'no!':
    await message.channel.send('Type in yes!')

# Third Command
  elif message.content == 'login!':
    await message.channel.send('Please go to ZKS RUSH ORTHO > login information in the shared drive')

# Fourth Command
  elif message.content == 'papersandtextbooks!':
    await message.channel.send('Navigate to ZKS RUSH ORTHO > Papers and Textbooks')

# Fifth Command
  elif message.content == 'instructionsandmeasurements!':
    await message.channel.send('Proceed to RUSH SPINE GROUP NEW > General Data Collection or RUSH SPINE GROUP NEW > Instructions/Directions > XR/MRI Measurement Instructions')

# Sixth Command
  elif message.content == 'tables!':
    await message.channel.send('Head on over to RUSH SPINE GROUP NEW > TABLES _instructions')

# Seventh Command
  elif message.content == 'otherquestion!':
    await message.channel.send('If I was unable to answer your question, please be sure to ask any of one the Team Leads :).')

client.run('NzI4NzI5NzY5MTYzNjIwNDc4.Xv-ofA.AHvCtJpUic8NAmnn5FKr4dX8E7E') # Unique Discord Token
