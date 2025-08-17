from tkinter import *
from tkcalendar import *
Window=Tk()
Window.geometry("400x500")
Window.title("calender")
Calendar(Window,selectmode="day",date_pattern="y-mm-dd",locale="en_US")



Window.mainloop()