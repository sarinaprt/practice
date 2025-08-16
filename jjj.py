from tkinter import *

window=Tk()
window.title("calculator")
window.geometry("180x300")

def add_en(x):
    entry.insert(0,text)

buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), (' . ', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('( ', 5, 1), (' )', 5, 2), ('^', 5, 3)
    ]
entry=Entry(window,font=("B nazanin",15),justify='right',relief='groove')
entry.grid(row=0,columnspan=4)

for (text,row,column) in buttons:
    butt=Button(window,bg="#48997D",text=text,width=5,height=3,command=lambda x=text: add_en(x))
    butt.grid(row=row,column=column)

window.mainloop()
