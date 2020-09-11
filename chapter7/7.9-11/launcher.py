from discord.ext import commands
import config
import asyncio
import discord

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


bot.load_extension("cogs.greet")  # この行を追加
bot.run(config.TOKEN)