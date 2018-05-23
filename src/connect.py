#Establishes connection to Discord servers

import discord
import asyncio
import getpass
import inquirer
from menu import *

#Gets username and password
def getUserInfo():
    username = input("Enter email address: ")

    #getpass works like Linux password entry. (Does not display chars for password)
    password = getpass.getpass("Enter password: ")

    info = {
        'username': username,
        'password': password,
        }
    return info

#Creates a scrollable server select
async def chooseServer(client):
    serverChoices = []
    for server in client.servers:
        serverChoices.append(server)
    selectedServer = [
        inquirer.List('server',
                      message = "Select a server",
                      choices = serverChoices
                      ),
        ]
    serverChoice = inquirer.prompt(selectedServer)
    return serverChoice['server']

#This doesn't work yet, will open submenu of channels to join once working
async def chooseChannel(client, server):
    clearScreen()
    showSplash()
    channelChoices = []
    channelIDs = []
    for channel in server.channels:
        channelChoices.append(channel.name)
        channelIDs.append(channel.id)
    selectedChannel = [
        inquirer.List('channel',
                      message = "Select a channel in " +
                      setTextColor(server.name, 'red'),
                      choices = channelChoices
                      ),
        ]
    channelChoice = inquirer.prompt(selectedChannel)
    return channelChoice['channel']

async def closeClient(client):
    await client.close()
