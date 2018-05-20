#Establishes connection to Discord servers

import discord
import asyncio
import getpass

#Gets username and password, move this inside of a function and call from a main python file
def getUserInfo():
    username = input("Enter username: ")
    #getpass works like Linux password entry. (Does not display chars for password)
    password = getpass.getpass("Enter password: ")
    #Currently a bot created through Discord API is required for this token
    #token = input("Enter token: ")

    print()
    info = {
        'username': username,
        'password': password,
        #'token': token
        }
    return info

#Discord.py may require async due to coroutines, this is here in that case
def loginClient(client, info):
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
