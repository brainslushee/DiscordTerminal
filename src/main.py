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
