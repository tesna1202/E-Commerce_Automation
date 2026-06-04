import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password