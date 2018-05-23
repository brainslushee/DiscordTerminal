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
from connect import getUserInfo, chooseServer, clearScreen#, closeClient

#Clears the screen so that the splashScreen is all that displays
clearScreen()

splashScreen = '''
----------------------------------------------------
   ____ ___ ____   ____ ___  ____  ____
  |  _ \_ _/ ___| / ___/ _ \|  _ \|  _ \\
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

userInfo = {}

#Creates scrollable list of login options, extrapolate this for other screens
#Maybe move into a function
loginOptions = [
    inquirer.List('choice',
                  message = "Login Menu",
                  choices = [
                      '1. use config file',
                      '2. enter email and password manually',
                  ],
                 ),
    ]

#Depending on loginOption selected, uses config or manual login. Maybe make into switch statement
menuChoice = inquirer.prompt(loginOptions)

if menuChoice == '1. use config file':
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
    await chooseServer(client)


#Runs Discord, be patient, receive times are somewhat slow.
#Add client.logout() and close() here to fix the unclosed session error
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(userInfo['username'], userInfo['password']))
