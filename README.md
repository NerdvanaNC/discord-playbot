# Discord Playbot
### PlayBot helps people find players on Discord.

**Commands**

- $help - displays this text.
- $play / $find - pings PlayBot subscribers.

If you're the Admin, please make a role with "PlayBot" in its name, this allows PlayBot to target that role specifically.

As a player, you can type "$play" or "$find" in any channel PlayBot has access to to ping other players. PlayBot only @mentions users with the admin-assigned PlayBot role.

I recommend disallowing the @mention ability for general users so they cannot abuse the PlayBot role by mentioning it w/o being "signed up" to receive alerts.

A Discord bot I'm making in Python to alert server members when a player is looking to play.

**Requires a role with "PlayBot" in its name**

(@todo ability for users to have their chosen role work with PlayBot)

> Disabling `@everyone's` ability to `@mention` prevents people from abusing the PlayBot role. They cannot `@PlayBot Role` people looking for players, but then decide to not "answer the call" when its their turn.

> Of course the entire bot is useless if people mute `@mentions` on the server, but I'll worry about that at a later date.

See `requirements.txt` for package requirements.

Passion project for my small server of 20-ish people.

© Nickunj Chopra (https://nickunjchopra.com) | *Copy karo magar pyaar se* **(Attributions Required)**