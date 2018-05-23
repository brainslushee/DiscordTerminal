#Establishes connection to Discord servers

import discord
import asyncio
import getpass
import inquirer
import os

#Gets username and password
def getUserInfo():
    username = input("Enter email address: ")
    
    #getpass works like Linux password entry. (Does not display chars for password)
    password = getpass.getpass("Enter password: ")
    print("One moment please, we are trying to connect...")
    
    info = {
        'username': username,
        'password': password,
        }
    return info

#Doesn't work yet... don't know why.
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

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

