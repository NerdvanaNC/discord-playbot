import discord
import os
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
        `PlayBot helps people looking for players find them.
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
        receive alerts.`
      """))
    return


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
    await message.channel.send("Sorry, I don't understand. Type \"$help\" for help.")

# Run PlayBot
client.run(DISCORD_BOT_TOKEN)