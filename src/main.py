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
from connect import getUserInfo, chooseServer, chooseChannel, messageFormat#, closeClient
from menu import showSplash, clearScreen, getLoginType, setTextColor, quit, openMenu
from client import printLoggedIn

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

@client.event
async def on_ready():
    clearScreen()
    showSplash()
    loggedInAs = 'Logged in as: ' + setTextColor(client.user.name, 'red')
    print(printLoggedIn(loggedInAs))

    #Defines server and channel
    global server
    global channel
    server = chooseServer(client)
    channel = chooseChannel(client, server)

    #Whoever gets this in an async loop wins the game
    chat = input(setTextColor(client.user.name + ": ", "red"))
    #Move to a function and make it a hotkey
    if chat == "MENU":
        menuChoice = openMenu()
        if menuChoice == 'Change Server':
            server = chooseServer(client)
        if menuChoice == 'Change Channel':
            channel = chooseChannel(client, server)
        if menuChoice == 'Exit Discord Terminal':
            quit()
    else:
        await client.send_message(channel, chat)

#Currently displays all messages from all servers. Still cool though.
@client.event
async def on_message(message):
    #Ensures that server and channel are set
    try:
        if channel == message.channel and server == message.server:
            print(messageFormat(message))
    except Exception as e:
        pass

#Runs Discord, be patient, receive times are somewhat slow.
#Add client.logout() and close() here to fix the unclosed session error
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(userInfo['username'], userInfo['password']))
#asyncio.ensure_future(writeMessage())
