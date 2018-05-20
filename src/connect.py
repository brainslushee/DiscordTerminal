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
async def loginClient(client, info):
    try:
        await client.login(info['username'], info['password'])
        print("Login successful: " + str(client.is_logged_in))
    except discord.errors.LoginFailure:
        print("Invalid login credentials. Login Failed.")
        print("Please try again.")

#Doesn't work yet... don't know why.
async def printServers(client):
    count = 1
    print("Available servers: ")
    for key in client.servers:
        print("\t{}. {}: {}".format(count, key, client.servers[key]))
        count += 1

async def closeClient(client):
    await client.close()
