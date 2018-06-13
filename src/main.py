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
import readline
import sys
import locale
from ConfigManager import ConfigManager
from Colors import Colors
from contextlib import suppress

#Add functions from connect as needed
from connect import getUserInfo, chooseServer, chooseChannel, messageFormat#, closeClient
from menu import showSplash, clearScreen, getLoginType, setTextColor, quit, openMenu
from client import printLoggedIn, chat

#Sets locale for curses
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
#Clears the screen so that the splashScreen is all that displays
clearScreen()
showSplash()

#Move this to client class eventually
client = discord.Client()

#This logs in user, maybe move to a function?
#Make to switch statement and add more options eventually
#tfw switch statements arent in python

#maybe move all of this into its own function?
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
    setConfig = ""
    while setConfig != "y" and setConfig != "n":
        setConfig = input("Would you like to set your config now for faster login? [y/n] ")

    if setConfig == "y":
        ConfigManager.setUserInfo(userInfo['username'], userInfo['password'])
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

    #Infinite loop that prompts for input...
    chatTask =  asyncio.Task(chat(client, server, channel))
    await asyncio.sleep(2)
    #chatTask.cancel()
    #with suppress(asyncio.CancelledError):
    #    await chatTask

#Currently displays all messages from all servers. Still cool though.
@client.event
async def on_message(message):
    receiveTask = asyncio.Task(printMessage(message))
    #await asyncio.sleep(2)
    #receiveTask.cancel()

async def printMessage(message):
    try:
        if channel == message.channel and server == message.server:
            if message.author == client.user:
                pass
            else:
                #line = str(sys.stdin.readline.get_line_buffer())
                print(messageFormat(message))
                #print(line)
    except Exception as e:
        pass

#Runs Discord, be patient, receive times are somewhat slow.
#Add client.logout() and close() here to fix the unclosed session error
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(userInfo['username'], userInfo['password']))
#asyncio.ensure_future(writeMessage())
