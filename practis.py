import re
import os
import calcU
import calender
from pydub import AudioSegment 
import sound_lib
# from pydub.playback import play
from pydub import playback


if not os.path.exists("username.txt"):
    with open("username.txt","w",encoding="utf-8")as f:
        f.write("")
        print("file_user_w")
if not os.path.exists("password.txt"):
    with open("password.txt","w",encoding="utf-8") as f:
        f.write("")
        print("file_user_r")

def id_play(id):
    if id in sound_lib.sound_so:
        file_path=sound_lib.sound_so.get(id)
        if os.path.exists(file_path):
            sound=AudioSegment.from_file(file_path).speedup(2)+20
            playback.play(sound)
    else:
        tens=int(id)//10
        unit=int(id)%10
        list_sound=[]
        if int(id)>20 and int(unit)!=0:
            if str(tens) in sound_lib.sound_so and str(unit) in sound_lib.sound_so:
                path_tens=sound_lib.sound_so.get(str(tens))
                path_unit=sound_lib.sound_so.get(str(unit))
                if os.path.exists(path_tens) and os.path.exists(path_unit):
                    list_sound.append(AudioSegment.from_file(path_tens))
                    list_sound.append(AudioSegment.from_file(sound_lib.sound_so.get("v")))
                    list_sound.append(AudioSegment.from_file(path_unit))
        for sou in list_sound:
            playback.play(sou)



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
            id=find_id.group(1).strip()
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
        chose=input(("you can choose : if you need to use calculator enter 1 if you need to write something in your note enter 2 if you wanna know about your id enter 3: "))
        if chose=="1":
            calcU.calculator()
        elif chose=="2":
            calender.calender_ac()
        elif chose=="3":
            id_play(id)



else:
    with open("password.txt","r",encoding="utf-8")as f:
        find_id=f.read()
        new_id=find_id.count(":")
    with open("username.txt","a",encoding="utf-8")as f :
        f.write(f"-{new_id}:{username}")
    with open("password.txt","a",encoding="utf-8")as f:
        f.write(f"-{new_id}:{password}")
    



