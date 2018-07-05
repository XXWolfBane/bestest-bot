import discord
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
    await ctx.send('Look Im alive!')
 
bot.run('NDY0NDYwMzEyMjUxMjAzNjI2.Dh_R4w.x0NU1_BMMB1Z613RYVe5DHTR-dg')
