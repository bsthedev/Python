from tkinter import *

log = Tk()
log.title("LOGIN")
log.geometry('300x200')

#Username Field
lbl1 = Label(log, text = "Username").grid(row = 0)
ent1 = Entry(log).grid(row = 0, column = 1) 

#Password Field
lbl2 = Label(log, text = "Password").grid(row = 1) 
ent2 = Entry(log).grid(row = 1, column = 1) 

#Login Button
btn = Button(log, text = 'Login').grid(row = 2, column = 1)

cb = Checkbutton(log, text = "Keep Me Logged In").grid(columnspan = 2) 

log.mainloop()