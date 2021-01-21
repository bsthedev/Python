from tkinter import *
from tkinter.ttk import *

base = Tk()
base.geometry('200x100')

#This button will close the window
btn_1 = Button(base, text ="Close Widget", command = base.destroy)
btn_1.pack(side = TOP)

#This button will close itself
btn_2 = Button(base, text ="Destroy top button", command = btn_1.destroy)
btn_2.pack(side = BOTTOM)

base.mainloop()
