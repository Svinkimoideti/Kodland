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
    await ctx.send(f'Привет! Я бот @{bot.user}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send(":regional_indicator_h: :regional_indicator_e: :regional_indicator_h: " * count_heh)
@bot.command()
async def ecology(ctx, eco=("Сдавайте стекло на переработку, Выключайте компьютер ночью, это поможет сэкономить до 1000 кВт ежемесячно, создание товара с разу уже из экологичных и переробатываемых материалов, В самом начале объяснить разницу между словами Экология и Окружающая среда.Позже рассказать о возмоных мерах ,которые можно предпринять, Сдавать на переработку как пластик ,так и стекло.В особенности сдавать алюминевые жестянки.1/3 запасов алюминия уходит на банки из-под газировки")):
    await ctx.send(eco)
@bot.command()
async def mem(ctx):
    images= os.listdir('images')
    img_name= random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")
