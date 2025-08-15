import re
import os

if not os.path.exists("username.txt"):
    with open("username.txt","w",encoding="utf-8")as f:
        f.write("")
    f.close()
if not os.path.exists("password.txt"):
    with open("password.txt","w",encoding="utf-8") as f:
        f.write("")
    f.close()

def enterys():
    username=input("Enter your usre name please: ")
    password=input("Enter your passwprd please: ")
    return username , password   

username,password=enterys()

while True:
    with open("username","r",encoding="utf-8")as f:
        lines_use=f.readlines()
    for line in lines_use:
        find_user=re.finditer(r"-\s+\d+:'(\w+)'",line)
        if find_user:        

            for find in find_user:
                print(find.group(0))
        else:
            print("Ff")
    break            
    



