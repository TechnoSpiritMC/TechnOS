import configparser

config = configparser.ConfigParser()

config.read('settings.properties')

print(dict(config.keys()))