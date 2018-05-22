#Establishes connection to Discord servers

import discord
import asyncio
import getpass

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
async def printServers(client):
    print("Available servers: ")
    for server in client.servers:
        print(server.name)
        
async def closeClient(client):
    await client.close()
