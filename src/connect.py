#Establishes connection to Discord servers

import discord
import asyncio


#Gets username and password, move this inside of a function and call from a main python file
def getUserInfo():
    username = input("Enter username: ")
    password = input("Enter password: ")
    #Currently a bot created through Discord API is required for this token
    #token = input("Enter token: ")

    print()
    info = {
        'username': username,
        'password': password,
        #'token': token
        }
    return info

async def loginClient(client, info):
    await client.login(info['username'], info['password'])
    print("Login successful?: " + str(client.is_logged_in))
