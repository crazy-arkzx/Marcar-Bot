import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
	
@bot.event
async def on_message(message):
    if message.author.bot:  # Evita que o Bot Responda as Marcacoes de Outros Bots
        return
    
    if bot.user in message.mentions:  # verifica se o bot foi mencionado
        await message.channel.send(f"Ola {message.author.mention}, Como Posso Ajudar?")
    
    await bot.process_commands(message)

bot.run("TOKEN")
