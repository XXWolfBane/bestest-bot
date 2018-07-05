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
    
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bestest Bot Help System", description="This is a list of all Bestest Bots commands!!", color=0xeee657)
    embed.add_field(name="alive", value="Displays magical text", inline=False)
    await ctx.send(embed=embed)
 
bot.run('NDYxOTUzNTk5NDI2MDAyOTU2.DiAAiQ.A2osYwBxq5Fh_tRixPL28aiLSFE')
