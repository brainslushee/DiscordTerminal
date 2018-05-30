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
from connect import getUserInfo, chooseServer, chooseChannel#, closeClient
from menu import showSplash, clearScreen, getLoginType, setTextColor, quit

#Clears the screen so that the splashScreen is all that displays
clearScreen()
showSplash()

#Move this to client class eventually
client = discord.Client()

#This logs in user, maybe move to a function?
#Make to switch statement and add more options eventually
userInfo = {}
loginType = getLoginType()
if loginType == 'Config File Login':
    #user ConfigManager class to get userInfo from json file
    config = ConfigManager()
    userInfo = config.getUserInfo()
    #use token from config file
elif loginType == 'Manual Login':
    #Gets username and password as a dictionary
    userInfo = getUserInfo()
else:
    quit()
print("One moment please, we are trying to connect...")
#Global variables for now...
@client.event
async def on_ready():
    clearScreen()
    showSplash()
    #Move this to a function
    hyphens = ""
    loggedInAs = 'Logged in as: ' + setTextColor(client.user.name, 'red')
    for x in range(0, len(loggedInAs) - 9):
        hyphens += "-"
    print(hyphens)
    print(loggedInAs)
    print(hyphens)
    global server
    global channel
    server = chooseServer(client)
    channel = chooseChannel(client, server)

    #Definitely move this to another function
    #It sends one message from YOU
    #chat = input("Say something: ")
    #await client.send_message(channel, chat)


#Currently displays all messages from all servers. Still cool though.
@client.event
async def on_message(message):
    try:
        if channel == message.channel and server == message.server:
            print(message.content)
    except Exception as e:
        pass
#Runs Discord, be patient, receive times are somewhat slow.
#Add client.logout() and close() here to fix the unclosed session error
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(userInfo['username'], userInfo['password']))
