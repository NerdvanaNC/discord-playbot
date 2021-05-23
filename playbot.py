import discord
import os
import random
from textwrap import dedent
from dotenv import load_dotenv

# Get the development environment variables
load_dotenv()

# Bot token from Discord
DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

# Init PlayBot
client = discord.Client()

@client.event
async def on_message(message):
  # We don't reply to messages sent by our own bot
  if message.author == client.user:
    return

  # Help message
  if message.content == "$help":
    await message.channel.send(dedent("""
        ```PlayBot helps people looking for players find them.
        ----
        Commands:
        > $help - displays this text.
        > $play / $find - pings PlayBot subscribers.
        ----
        If you're the Admin, please make a role with "PlayBot" in its name,
        this allows PlayBot to target that role specifically.

        As a player, you can type "$play" or "$find" in any channel PlayBot
        has access to to ping other players. PlayBot only @mentions users
        with the admin-assigned PlayBot role.

        I recommend disallowing the @mention ability for general users so they
        cannot abuse the PlayBot role by @mentioning it w/o being "signed up" to
        receive alerts.```
      """))
    return

  n_quotes = os.environ.get('N_QUOTES').split(", ")
  b_quotes = os.environ.get('B_QUOTES').split(", ")
  j_quotes = os.environ.get('J_QUOTES').split(", ")
  s_quotes = os.environ.get('S_QUOTES').split(", ")
  t_quotes = os.environ.get('T_QUOTES').split(", ")

  if message.content.find("nerd") != -1:
    await message.channel.send("> \"" + n_quotes[(random.randint(0, (len(n_quotes) - 1)))] + "\"\n - Nerdybhaiya urf Nerd")
    return

  if message.content.find("bacchi") != -1 or message.content.find("bachhi") != -1:
    await message.channel.send("> \"" + b_quotes[(random.randint(0, (len(b_quotes) - 1)))] + "\"\n - BacchiBhaiyu urf Bacchi")
    return

  if message.content.find("nova") != -1:
    await message.channel.send("> \"" + j_quotes[(random.randint(0, (len(j_quotes) - 1)))] + "\"\n - Nauja urf Nova")
    return

  if message.content.find("95") != -1:
    await message.channel.send("> \"" + s_quotes[(random.randint(0, (len(s_quotes) - 1)))] + "\"\n - Jangababa urf 95")
    return

  if message.content.find("thakur") != -1:
    await message.channel.send("> \"" + t_quotes[(random.randint(0, (len(t_quotes) - 1)))] + "\"\n - Thakurain urf Chinki")
    return

  if message.content.find("gate") != -1:
    await message.channel.send("> DARWAZA HOTA HAI BHEN****")

  # Call message
  if message.content == "$play" or message.content == "$find":
    # Someone invoked PlayBot
    playBotRole = None
    authorAuth = None
    # let's get a list of all roles in the guild
    for guildRole in message.author.guild.roles:
      # check which role is "PlayBot Subscriber" or equivalent
      # with "PlayBot" in its name. Having a role with "PlayBot" in
      # its name is a requirement for now.
      # @todo allow users to pass in a custom role for use with PlayBot
      if guildRole.name.find("PlayBot") != -1:
        playBotRole = guildRole
        break
      
    if playBotRole:
      # check if the message.author is subscribed to the playBotRole
      for authorRole in message.author.roles:
        if authorRole.id == playBotRole.id:
          authorAuth = True
          break
      
      if authorAuth == True:
        # if yes - then send a mention to that role
        await message.channel.send(
          "{} hey everyone! {} is looking to play!".format(playBotRole.mention, message.author.name))
        return
      else:
        # else tell the author that they need to self-assign the role to call others
        await message.channel.send(
          "{} - you aren't subscribed to the \"{}\" role; you need to be a subscriber before you can call others.".format(
            message.author.mention, playBotRole))
        return
    else:
      await message.channel.send(
      "PlayBot can't find a \"PlayBot\" role in your server.\
      \nPlease make a role with the word \"PlayBot\" in its name for PlayBot to use.")
      return
  else:
    return

# Run PlayBot
client.run(DISCORD_BOT_TOKEN)