input discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def onready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    
@bot.command()
async def alive(ctx):
    ctx.send('Look I'm alive!")
 
