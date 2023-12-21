from commands import *


while True:
    debugMode = False
    command = input("> ")
    
    if command == "help":
        print(f"Help:\n")
            
    if command == "exit":
        exit()
        
           
    if str(command[0:2]) == "cd":
        cd(command[3:])
        
    if str(command[0:4]) == "echo":
        echo(command[5:])
        
    if str(command[0:5]) == "clear":
        clear()
        
    if str(command[0:3]) == "cat":
        cat(command[5:])
            
