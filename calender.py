from tkinter import *
from tkcalendar import *
import re
import os
if not os.path.exists("note.txt"):
    with open("note.txt","w",encoding="utf-8")as f:
        f.write()
        
def Diary_not(event):
    global entr
    global date
    second_page=Toplevel()
    date=calend.get_date()
    second_page.title(f"{date}")
    second_page.geometry("400x400")
    entr=Text(second_page,font=("B Nazanin ",12))
    with open("note.txt","r",encoding="utf-8")as f:
        read_folder=f.readlines()
    for line in read_folder:
        note=re.search(rf"-{date}:(.+)",line)
        if note:
            notee=note.group(1)
            entr.insert(1.0,notee)
            break
    else:
        entr.insert(1.0,"enter your daliy rotin")
    entr.bind("<FocusIn>",type_tim)
    entr.bind("<FocusOut>",stop_typ)
    entr.place(width=400,height=300)
    but=Button(second_page,text="apply",command=save).place(x=150,y=350,width=100)  
    but=Button(second_page,text="change",command=update).place(x=50,y=350,width=100)

def update():
    new_note=entr.get(1.0,END)
    if new_note!="enter your daliy rotin":
        with open("note.txt","r",encoding="utf-8")as f:
            lin_up=f.readlines()
        for lin in lin_up:
            if lin.startswith(f"-{date}:"):
                change_note=re.sub(rf"-{date}:.*",fr"-{date}:{new_note}",lin)
                print(change_note)
                entr.insert(1.0,change_note)

def type_tim(event):
    if entr.get(1.0,END).strip()=="enter your daliy rotin":
        entr.delete(1.0,END)

def stop_typ(event):
    if entr.get(1.0,END).strip()=="":
        entr.insert(1.0,"enter your daliy rotin")
def save():
    writ=entr.get(1.0,END)
    with open("note.txt","a",encoding="utf-8")as f:
        f.writelines(f"-{date}:{writ}")



Window=Tk()
Window.geometry("400x500")
Window.title("calender")
calend=Calendar(Window,selectmode="day",date_pattern="y-mm-dd",locale="en_US")
calend.bind("<<CalendarSelected>>",Diary_not)
calend.pack(fill="both",expand=True)


Window.mainloop()