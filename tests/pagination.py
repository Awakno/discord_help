import discord
from discord.ext import commands
from discord_help import Pagination  # Replace with the actual file path

bot = discord.Bot(intents=discord.Intents.all())

@bot.slash_command()
async def test_pagination(ctx):
    pages = [discord.Embed(title="Page 1"), discord.Embed(title="Page 2")]
    view = Pagination(author=ctx.author, pages=pages, embeded=True)
    message = await ctx.send(content="Placeholder message for pagination", view=view)
    

    
bot.run("MTE3MDgwMzUwMTQxMzE4MzU1OQ.GKNmhr.A9vKnQIQ_y4KopS04ETckFgjywEEKSwetbGaak")