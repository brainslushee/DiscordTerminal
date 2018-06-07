import json
import os

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

    def setUserInfo(username, password):
        configFile = "../config/config.json"
        with open(configFile, 'r') as f:
            data = json.load(f)
            data['username'] = username
            data['password'] = password

            os.remove(configFile)
            with open(configFile, 'w') as f:
                json.dump(data, f, indent=4)

    def readJSON(self, configFile):
        '''
        Reads in json config file located in
        the config directory
        '''
        with open(configFile) as jsonFile:
            loginCredentials = json.load(jsonFile)
            self.username = loginCredentials["username"]
            self.password = loginCredentials["password"]
