from commands import commandClass

while True:
    command = input("> ")
    
    if command in commandClass.commandList:
        if command.startswith("cd"):
            for char in command:
                if char == " ":
                    spaceAdress = char
            print(commandClass.cd(command.split(" ")[1]))
            
        if command == "help":
            print(f"Help:\n{commandClass.commandList}")