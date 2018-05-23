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
import inquirer
from ConfigManager import ConfigManager
from Colors import Colors

#Add functions from connect as needed
from connect import getUserInfo, chooseServer#, closeClient
from menu import showSplash, clearScreen, getLoginType

#Clears the screen so that the splashScreen is all that displays
clearScreen()
showSplash()

#Move this to client class eventually
client = discord.Client()

#This logs in user, maybe move to a function?
#Make to switch statement and add more options eventually
userInfo = {}
loginType = getLoginType()
if loginType == '1. use config file':
    #user ConfigManager class to get userInfo from json file
    config = ConfigManager()
    userInfo = config.getUserInfo()
    #use token from config file
else:
    #Gets username and password as a dictionary
    userInfo = getUserInfo()
    
print("One moment please, we are trying to connect...")

@client.event
async def on_ready():
    clearScreen()
    hyphens = ""
    loggedInAs = 'Logged in as: ' + client.user.name
    for x in range(0, len(loggedInAs)):
        hyphens += "-"
    print(hyphens)
    print(loggedInAs)
    print(hyphens)
    await chooseServer(client)


#Runs Discord, be patient, receive times are somewhat slow.
#Add client.logout() and close() here to fix the unclosed session error
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(userInfo['username'], userInfo['password']))
