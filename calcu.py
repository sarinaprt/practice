from tkinter import *


def calculator():
    def add_en(x):
        en=entry.get()
        entry.delete(0,END)
        entry.insert(END,en+x)

    def eva():
        try:
            en=entry.get()
            answer=eval(en)
            entry.delete(0,END)
            entry.insert(END,answer)
        except ZeroDivisionError:
            entry.delete(0,END)
            entry.insert(END,"you cant divide by zero")
        except SyntaxError:
            entry.delete(0,END)
            entry.insert(END,"you have syntax error")
        except Exception:
            entry.delete(0,END)
            entry.insert(END,"there is something wrong")



    def delet():
        entry.delete(0,END)

    window=Tk()
    window.title("calculator")
    window.geometry("180x300")


    buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), (' . ', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('( ', 5, 1), (' )', 5, 2), ('^', 5, 3)
        ]
    entry=Entry(window,text="enter your number",font=("B nazanin",15),justify='right',relief='groove')
    entry.grid(row=0,columnspan=4)

    for (text,row,column) in buttons:
        if text=="=":
            butt=Button(window,bg="#48997D",text=text,relief='groove',height=3,width=5,command=eva)
        elif text=="C":
            butt=Button(window,bg="#48997D",text=text,relief='groove',height=3,width=5,command=delet)
        else:
            butt=Button(window,bg="#48997D",text=text,relief='groove',width=5,height=3,command=lambda x=text: add_en(x))
        butt.grid(row=row,column=column)



    window.mainloop()
