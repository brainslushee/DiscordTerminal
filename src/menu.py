from Colors import Colors
import os
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
    colors = Colors()

    print(colors.Foreground.purple, splashScreen)
    colors.resetColors()

#Call this to clear terminal screen for clean UI
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def getLoginType():
    #Creates scrollable list of login options, extrapolate this for other screens
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
    loginType = inquirer.prompt(loginOptions)
    return loginType['choice']
