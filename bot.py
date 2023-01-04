import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "jay" in message.content.lower():
        await message.channel.send('Jay, otherwise known as Jay Garcia Felipe Marzia, is a anon American of unknown '
                                   'weight '
                                   'perhaps, obese.')

    if "seb" in message.content.lower():
        await message.channel.send('Do not speak of the British man.')

client.run(TOKEN)
