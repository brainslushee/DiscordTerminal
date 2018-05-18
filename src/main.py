#To get discord.py: sudo python -m pip install -U discord.py
#To get asyncio: sudo python -m pip install -U asyncio
#May want to put the above in a .sh file
import discord
import asyncio

#Add functions from connect as needed
from connect import getUserInfo, loginClient

#Gets username and password as a dictionary
userInfo = getUserInfo()

#Move this to client class eventually
client = discord.Client()

#Trying to implement asyncio on connect.py
#client.login(userInfo['username'], userInfo['password'])
#client.connect()

loop = asyncio.get_event_loop()
loop.run_until_complete(loginClient(client, userInfo))
loop.close()

#Prints if login is successful
print("Successful login: " + str(client.is_logged_in))
