from Colors import Colors
import os
import sys
import inquirer

#Shows the splash screen
def showSplash():

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
    #create colors object for use in formatting colored terminal output

    print(setTextColor(splashScreen, 'purple'))

#Call this to clear terminal screen for clean UI
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def quit():
    clearScreen()
    sys.exit()

def openMenu():

    menuOptions = [
        inquirer.List('option',
                      message = "Menu",
                      choices = [
                         'Change Server',
                         'Change Channel',
                         'Exit Discord Terminal',
                      ],
                     ),
    ]
    menuSelection = inquirer.prompt(menuOptions)
    return menuSelection['option']

#Sets text color, may need to move to more appropriate file
def setTextColor(text, colorChoice):
    colors = Colors()
    setColor = getattr(colors.Foreground, colorChoice)
    coloredText = setColor + text + colors.reset
    return coloredText

def getLoginType():
    #Creates scrollable list of login options, extrapolate this for other screens
    loginOptions = [
        inquirer.List('choice',
                      message = "Login Type",
                      choices = [
                          'Config File Login',
                          'Manual Login',
                          'Exit',
                      ],
                     ),
        ]

    #Depending on loginOption selected, uses config or manual login. Maybe make into switch statement
    loginType = inquirer.prompt(loginOptions)
    return loginType['choice']
