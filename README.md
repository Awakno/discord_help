# Discord_help
## Overview

Discord_help is a powerful and easy-to-use library for Discord bots.

## Installation
Use pip

```bash
pip install discord_help
```
Or use Git
```bash
git clone https://github.com/Awakno/discord_help.git
```


## Usage

### Pagination

Create your own pagination menu with Discord_help

```python

import discord
import discord_help


@bot.command()
async def pagination():
    pages = [discord.Embed(title="Page 1"), discord.Embed(title="Page 2")]
    view = discord_help.Pagination(author=ctx.author,error_message=discord.Embed(description="`❌`**Tu n'as pas la permission d'utiliser ce menu**"), pages=pages,embeded=True)
    message = await ctx.send(content="Placeholder message for pagination", view=view)

bot.run("TOKEN")
```

### Invite tracker 

Track invitation on join

```python
import discord
import discord_help

bot = discord.Bot(intents=discord.Intents.all())

tracker = discord_help.Invite(bot)

@bot.event
async def on_member_join(member):
    invites=await tracker.on_member_join(member)
    print(f"{member} joined with discord.gg/{invites.code}")
```

### Parse time 

```python
import discord
import discord_help

@bot.command()
async def parse_time(ctx, time):
    # time -> 1d
    timespan = discord_help.parse_timespan(time)
    await ctx.send(timespan)
    # -> 86400
```

# Credits

##### Author: Awakno
##### Contact: awaknocode@gmail.com
##### Discord: https://discord.gg/TzreuU5a7A

