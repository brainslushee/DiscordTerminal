#  ____ ___ ____   ____ ___  ____  ____  
# |  _ \_ _/ ___| / ___/ _ \|  _ \|  _ \ 
# | | | | |\___ \| |  | | | | |_) | | | |
# | |_| | | ___) | |__| |_| |  _ <| |_| |
# |____/___|____/ \____\___/|_| \_\____/ 
#   _____ _____ ____  __  __ ___ _   _    _    _     
# |_   _| ____|  _ \|  \/  |_ _| \ | |  / \  | |    
#   | | |  _| | |_) | |\/| || ||  \| | / _ \ | |    
#   | | | |___|  _ <| |  | || || |\  |/ ___ \| |___ 
#   |_| |_____|_| \_\_|  |_|___|_| \_/_/   \_\_____|
#                                                   

import discord
import asyncio
from ConfigManager import ConfigManager

#Add functions from connect as needed
from connect import getUserInfo, getToken#, printServers, closeClient

#this is a temporary menu that could be extracted into a function
print("Login Menu: ")
print("\t1. use config file")
print("\t2. enter email and password manually")
menuChoice = int(input("\t>>> "))

userInfo = {}

if menuChoice == 1:
    #user ConfigManager class to get userInfo from json file
    config = ConfigManager()
    userInfo = config.getUserInfo()
else:
    #Gets username and password as a dictionary
    userInfo = getUserInfo()


#Move this to client class eventually
client = discord.Client()

token = getToken(client, userInfo)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("Available servers: ")
    for server in list(client.servers):
        print(server.name)

#Runs Discord, be patient, receive times are somewhat slow.
client.run(token, bot=False)
