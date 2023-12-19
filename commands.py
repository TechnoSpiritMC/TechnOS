import os

class commandClass:
    commandList = ["cd", "ls", "help"]
    
    def cd(target):
        return os.scandir(target)