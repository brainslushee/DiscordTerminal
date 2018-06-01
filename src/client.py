#Client class for Discord

import discord
import asyncio
from connect import chooseServer, chooseChannel
from menu import setTextColor, openMenu

#client = discord.Client()

def printLoggedIn(loggedInAs):
    hyphens = ""
    for x in range(0, len(loggedInAs) - 9):
        hyphens += "-"
    print(hyphens)
    print(loggedInAs)
    print(hyphens)

#Used in main to allow user to chat
async def chat(client, server, channel):
    while True:
        message = input(setTextColor(client.user.name + ": ", "red"))
        #Move to a function and make it a hotkey
        if message == "MENU":
            menuChoice = openMenu()
            if menuChoice == 'Change Server':
                server = chooseServer(client)
            if menuChoice == 'Change Channel':
                channel = chooseChannel(client, server)
            if menuChoice == 'Exit Discord Terminal':
                quit()
        else:
            await client.send_message(channel, message)
        await asyncio.sleep(1)
