import nextcord
import config
import os
from nextcord.ext import commands
from keep_alive import keep_alive

keep_alive()

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name} ({bot.user.id})')
    print('---------------------------------------------')
    print('You can fuck w/ the bot now!!!')
    print("===============================")

# load cogs 
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')







bot.run(config.TOKEN)