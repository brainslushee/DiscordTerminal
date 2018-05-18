#Client class for Discord

import discord
import asyncio

#client = discord.Client()

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#client.close()
