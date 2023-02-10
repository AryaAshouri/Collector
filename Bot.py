from discord.ext import commands
from Scraper import pollution
from Scraper import temperature
bot = commands.Bot(command_prefix = "")

@bot.event
async def on_ready():
    print(">> Bot is ready")

@bot.event
@commands.has_permissions(manage_messages=True)
async def on_message(message):

    if (message.content == "show pollution"):
        await pollution(message)

    if (message.content == "show temperature"):
        await temperature(message)

bot.run("DISCORD_TOKEN")