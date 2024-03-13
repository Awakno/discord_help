import discord
import discord_help

bot = discord.Bot(intents=discord.Intents.all())


@bot.slash_command()
async def test(ctx):
    error_message = discord.Embed(description="`❌` **Tu n'as pas la permission d'utiliser ce menu**")
    pagination = discord_help.Pagination(
        author=ctx.author,
        pages=[
            discord.Embed(title="Page 1"),
            discord.Embed(title="Page 2"),
            discord.Embed(title="Page 3")
        ],
        embeded=True,
        error_message=error_message
    )
    
    timespan = discord_help.parse_timespan("1h")
    await ctx.respond(content=timespan,view=pagination)

tracker = discord_help.Invite(bot)    

@bot.event
async def on_member_join(member):
    inv = await tracker.fetch_invite(member)
    print(inv.code)

    
    

    

<<<<<<< HEAD
bot.run("")
=======
bot.run("TOKEN")
>>>>>>> 605088d836d83bd6fcd9df71257a04e8ad273c18
