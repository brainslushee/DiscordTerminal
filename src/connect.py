#Establishes connection to Discord servers

import discord
import asyncio
import getpass
import inquirer

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
        serverChoices.append(server.name)
    selectedServer = [
        inquirer.List('server',
                      message = "Select a server",
                      choices = serverChoices
                      ),
        ]
    serverChoice = inquirer.prompt(selectedServer)

async def closeClient(client):
    await client.close()
