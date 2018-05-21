class Colors:
    '''
    Example usage:
        print(Colors.Foreground.purple, "here is some text")

    These escape sequences for colors just need to be put before
    whatever you're trying to print. Don't forget to reset the 
    colors. 
    '''   
    
    def __init__(self):
        self.reset='\033[0m'
        self.bold='\033[01m'
        self.disable='\033[02m'
        self.underline='\033[04m'
        self.reverse='\033[07m'
        self.strikethrough='\033[09m'
        self.invisible='\033[08m'

    def resetColors(self):
        #called to reset the color palete
        print(self.reset)

    class Foreground:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class Background:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
