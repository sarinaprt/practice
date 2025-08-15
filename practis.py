import re
import os

if not os.path.exists("username.txt"):
    with open("username.txt","w",encoding="utf-8")as f:
        f.write("")
        print("file_user_w")
    f.close()
if not os.path.exists("password.txt"):
    with open("password.txt","w",encoding="utf-8") as f:
        f.write("")
        print("file_user_r")
    f.close()

def enterys():
    username=input("Enter your usre name please: ")
    password=input("Enter your passwprd please: ")
    return username , password  
 
id=None
password_find=None
username,password=enterys()
with open("username.txt","r",encoding="utf-8")as f:
    lines_use=f.readlines()
for line in lines_use:
    find_id=re.search(fr"-\s+(\d+):'{username}'",line)
    if find_id:        
            id=find_id.group(1)
            break

if id:
    with open("password.txt","r",encoding="utf-8")as f:
        line_pass=f.readlines()
    for lin_p in line_pass:
        pas=re.search(fr"-\s*{id}:\s*'(.+?)'\s*",lin_p)
        if pas:
            password_find=pas.group(1).strip()
            break
    if password_find==password:
        chose=input(int("you can choose : if you need to use calculator enter 1if you need to write something in your note enter 2 if you wanna know about your id enter 3"))
        if chose=="1":
            pass

else:
    pass
    



