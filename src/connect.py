#Establishes connection to Discord servers

import discord
import asyncio
import getpass

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

#Gets token to run program
def getToken(client, info):
    try:
        client.login(info['username'], info['password'])
        print("Login successful: " + str(client.is_logged_in))
        token = str(client._get_cache_token(info['username'], info['password']))
        return token
    except discord.errors.LoginFailure:
        print("Invalid login credentials. Login Failed.")
        print("Please try again.")
        
#Doesn't work yet... don't know why.
async def printServers(client):
    print("Available servers: ")
    for server in client.servers:
        print(server.name)
        
async def closeClient(client):
    await client.close()
