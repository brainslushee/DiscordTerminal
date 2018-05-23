import json

class ConfigManager:
    def __init__(self):
        configFile = "../config/config.json"
        self.username = ""
        self.password = ""
        self.readJSON(configFile)

    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password

    def getUserInfo(self):
        '''
        Returns a dictionary of userInfo to be used
        when logging with the client
        '''
        info = {
                'username': self.username,
                'password': self.password,
              }
        return info

    def readJSON(self, configFile):
        '''
        Reads in json config file located in
        the config directory
        '''
        with open(configFile) as jsonFile:
            loginCredentials = json.load(jsonFile)
            self.username = loginCredentials["username"]
            self.password = loginCredentials["password"]
