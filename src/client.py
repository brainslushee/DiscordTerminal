#Client class for Discord

import discord
import asyncio

#client = discord.Client()

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def printLoggedIn(loggedInAs):
    hyphens = ""
    for x in range(0, len(loggedInAs) - 9):
        hyphens += "-"
    print(hyphens)
    print(loggedInAs)
    print(hyphens)
