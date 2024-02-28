pip install discord.py
import discord
from discord.ext import commands
import datetime

# Initialize the bot
bot = commands.Bot(command_prefix='!')

# Dictionary to store user birthdays (user_id: birthday)
user_birthdays = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def set_birthday(ctx, date):
    try:
        user_birthdays[ctx.author.id] = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        await ctx.send(f"Your birthday has been set to {date}!")
    except ValueError:
        await ctx.send("Please use the format YYYY-MM-DD to set your birthday.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if it's the user's birthday and send a message
    user_id = message.author.id
    today = datetime.date.today()
    if user_id in user_birthdays and user_birthdays[user_id] == today:
        await message.channel.send(f"Happy Birthday, {message.author.mention}!")

    await bot.process_commands(message)
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
