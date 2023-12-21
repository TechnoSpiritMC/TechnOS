import os

    
def cd(target):
    print(os.listdir(target))
    
def echo(text):
    print(text)
        
def clear():
    for i in range(150):
        print("\n")
        
def cat(path):
    if os.path.exists(path):
        print("a")
        with open(path, "r") as file:
            _content = file.readlines()
            file.close()
        print(_content)
        
    print("b")
    
    