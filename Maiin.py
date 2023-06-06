import discord
from discord.ext import commands
import os
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)
@bot.command()
async def mem(ctx):
    images= os.listdir('images')
    img_name= random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("MTEwOTM4NDkzMDA0NTIxMDc1OA.GseLzS.U0BG959JBemxZxlrqfEZfxCz8f7pR0RGKABIcM")
