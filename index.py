import discord, os, re, time
from dotenv import load_dotenv
load_dotenv()
from discord.ext import commands
from validate_email import validate_email

bot = commands.Bot(command_prefix='!') # fix bot prefix
#regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # set regex for checking email
bot.remove_command('help')

""" def check(email):   
  
    if(re.search(regex,email)):   # noob way of checking
        return True  
    else:   
        return False """

@bot.command()
async def ping(ctx):
    await ctx.send('My ping is {0}'.format(round(bot.latency, 1))) # return bot latency

@bot.command()
async def purge(ctx):
    await ctx.channel.purge(limit=2) # purge sign up message after sending

@bot.command()
async def smu(ctx, arg):
    if validate_email(arg,verify=True):
        await ctx.send("Thank you for signing up, " + arg) # if email is valid
        # add code for storing in db 
        time.sleep(2)
        await purge(ctx)
    else: 
        await ctx.send("Please enter a valid email address") # if email is invalid
        time.sleep(2)
        await purge(ctx)

@bot.group(invoke_without_command = True) 
async def help(ctx):
    embedVar = discord.Embed(title="Help Command", description="At your service! To learn about individual commands, type `!help <cmd name>`", color=0x805ebf) # create embed for help cmd
    embedVar.add_field(name="ping", value="Tells you how slow the bot is aka the bot's latency", inline=False)
    embedVar.add_field(name="smu <email>", value="Adds you to the mailing list IF your email ID is valid", inline=False)
    await ctx.channel.send(embed=embedVar)

@help.command()  
async def ping(ctx):
    embedVar = discord.Embed(title="ping Command", description="So you wanna play huh? :ping_pong: ", color=0xf63836) # create embed for help subcommand
    embedVar.add_field(name="ping", value="Tells you how slow the bot is aka the bot's latency", inline=False)
    await ctx.channel.send(embed=embedVar)

@help.command()  
async def smu(ctx):
    embedVar = discord.Embed(title="smu Command", description="We wanna slide in your DMs, let us? :sweat_smile:", color=0x114635) # create embed for help subcommand
    embedVar.add_field(name="smu <email>", value="`!smu <email>`: Adds you to the mailing list IF your email ID is valid", inline=False)
    await ctx.channel.send(embed=embedVar)

bot.run(os.getenv('DISCORD_TOKEN')) # you'll never know my secret 🤫