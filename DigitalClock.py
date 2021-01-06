import time
from tkinter import *
clock = Tk()
clock.title("Digital Clock")
clock.geometry("470x125")
clock.resizable(1,1)
dc = Label(clock, font=("Times New Roman", 30, 'bold'), bg="red", fg="black", bd = 35)
dc.pack(pady=40)
dc.grid(row=0, column=1)
def digitalclock():
   text_input = time.strftime("%H:%M:%S - %d/%m/%y")
   dc.config(text=text_input)
   dc.after(300, digitalclock)
digitalclock()
dc.mainloop()