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
        
    def readJSON(self, configFile):
        with open(configFile) as jsonFile:
            loginCredentials = json.load(jsonFile)
            self.username = loginCredentials["username"]
            self.password = loginCredentials["password"]

