import time
from tkinter import *
canvas = Tk()
canvas.title("Digital Clock")
canvas.geometry("470x125")
canvas.resizable(1,1)
label = Label(canvas, font=("Times New Roman", 30, 'bold'), bg="red", fg="black", bd = 35)
label.grid(row=0, column=1)
def digitalclock():
   text_input = time.strftime("%H:%M:%S - %d/%m/%y")
   label.config(text=text_input)
   label.after(300, digitalclock)
digitalclock()
canvas.mainloop()