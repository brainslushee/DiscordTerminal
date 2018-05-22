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
from Colors import Colors

#Add functions from connect as needed
from connect import getUserInfo#, printServers, closeClient

splashScreen = '''
----------------------------------------------------
  ____ ___ ____   ____ ___  ____  ____  
  |  _ \_ _/ ___| / ___/ _ \|  _ \|  _ \ 
  | | | | |\___ \| |  | | | | |_) | | | |
  | |_| | | ___) | |__| |_| |  _ <| |_| |
  |____/___|____/ \____\___/|_| \_\____/ 
    _____ _____ ____  __  __ ___ _   _    _    _     
  |_   _| ____|  _ \|  \/  |_ _| \ | |  / \  | |    
    | | |  _| | |_) | |\/| || ||  \| | / _ \ | |    
    | | | |___|  _ <| |  | || || |\  |/ ___ \| |___ 
    |_| |_____|_| \_\_|  |_|___|_| \_/_/   \_\_____|
----------------------------------------------------
    '''
#Move this to client class eventually
client = discord.Client()

#create colors object for use in formatting colored terminal output
colors = Colors()

print(colors.Foreground.purple, splashScreen)
colors.resetColors()

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
    #use token from config file
else:
    #Gets username and password as a dictionary
    userInfo = getUserInfo()

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('------')
    print("Available servers: ")
    for server in list(client.servers):
        print(server.name)

#Runs Discord, be patient, receive times are somewhat slow.
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(userInfo['username'], userInfo['password']))
