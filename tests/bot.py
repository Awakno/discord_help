import discord
import discord_help

bot = discord.Bot(intents=discord.Intents.all())


@bot.slash_command()
async def test(ctx):
    pagination = discord_help.Pagination(
        author=ctx.author,
        pages=[
            discord.Embed(title="Page 1"),
            discord.Embed(title="Page 2"),
            discord.Embed(title="Page 3")
        ],
        embeded=True
    )
    
    timespan = discord_help.parse_timespan("1h")
    await ctx.respond(content=timespan,view=pagination)

tracker = discord_help.Invite(bot)    

@bot.event
async def on_member_join(member):
    inv = await tracker.fetch_invite(member)
    print(inv.code)

    
    

    

bot.run("MTE3MDgwMzUwMTQxMzE4MzU1OQ.GN6YBs.bFyWKenz7uFCk6yFZAQ6WoL7A-fCpqeTsExSpY")