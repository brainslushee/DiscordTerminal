#To get discord.py: sudo python -m pip install -U discord.py
#To get asyncio: sudo python -m pip install -U asyncio
#May want to put the above in a .sh file
import discord

#Add functions from connect as needed
from connect import getUserInfo

#Gets username and password as a dictionary
userInfo = getUserInfo()

#Move this to client class eventually
client = discord.Client()

client.login(userInfo['username'], userInfo['password'])
