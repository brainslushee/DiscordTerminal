#To get discord.py: sudo python -m pip install -U discord.py
#To get asyncio: sudo python -m pip install -U asyncio
#May want to put the above in a .sh file
import discord
import asyncio

#Add functions from connect as needed
from connect import getUserInfo, loginClient, printServers, closeClient

#Gets username and password as a dictionary
userInfo = getUserInfo()

#Move this to client class eventually
client = discord.Client()

#Logs in client within a loop, move into a function
loop = asyncio.get_event_loop()
loop.run_until_complete(loginClient(client, userInfo))
loop.run_until_complete(printServers(client))
loop.run_until_complete(closeClient(client))
loop.close()
