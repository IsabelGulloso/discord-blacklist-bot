import discord
import requests
import asyncio
import csv
from io import StringIO

import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1482348854518091911
MESSAGE_ID = 1482381120325681263
SHEET_URL = "https://docs.google.com/spreadsheets/d/1g6cTzwA4h7EH1K7nBqOn1uVR2FNfMSPg1tT0_0z-WUc/export?format=csv"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def actualizar():

    await client.wait_until_ready()
    channel = await client.fetch_channel(CHANNEL_ID)
    message = await channel.fetch_message(MESSAGE_ID)

    while True:

try:
    r = requests.get(SHEET_URL)
    data = list(csv.reader(StringIO(r.text)))
except:
    print("Error leyendo Google Sheets")
    await asyncio.sleep(60)
    continue

        texto = "📋 **Lista Actualizada**\n\n"

        for row in data[1:]:
            texto += f"• {row[0]} — {row[1]}\n"

        await message.edit(content=texto)

        await asyncio.sleep(300)

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")
    client.loop.create_task(actualizar())

client.run(TOKEN)
