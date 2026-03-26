import os
import discord
from transcriber import transcribe
from discord.ext import commands
import assemblyai as aai
from dotenv import *

load_dotenv()
api_key = os.getenv("ASSEMBLYAI_API_KEY")

token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)

base_url = "https://api.assemblyai.com/v2"
headers = {
    "authorization": api_key
}

@bot.event
async def on_ready():
    print("We are ready to go!")

@bot.event
async def on_message(message):
    print("Message received:", message.content)
    print("Attachments:", message.attachments)
    print("Embeds:", message.embeds)

    if message.author == bot.user:
        return
 
    for attachment in message.attachments:
        if attachment.filename.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a')):
            audio = await attachment.read()
            transcript_text = transcribe(audio)
            await message.channel.send(f"{message.author.mention} - {transcript_text}")
    
    if not message.attachments and not message.embeds and not message.content.strip():
        await message.channel.send(
        f"Sorry {message.author.mention}, I can’t transcribe Discord voice messages. "
        "Please upload the audio file instead."
    )

    await bot.process_commands(message)

bot.run(token)