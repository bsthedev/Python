from tkinter import *
from tkinter import ttk
reg = Tk()
reg.title("Registration Form")
reg.geometry('400x400')
reg.configure(background = "grey")

''' Data Names ''' 

a = Label(reg ,text = "First Name", font = ('Times New Roman',10,'bold'),
          fg = 'black').grid(row = 0,column = 0)
b = Label(reg ,text = "Last Name",font = ('Times New Roman',10,'bold'),
          fg = 'black').grid(row = 1,column = 0)
c = Label(reg ,text = "Email Id",font = ('Times New Roman',10,'bold'),
          fg = 'black').grid(row = 2,column = 0)
d = Label(reg ,text = "Contact Number",font = ('Times New Roman',10,'bold'),
          fg = 'black').grid(row = 3,column = 0)
e = Label(reg ,text = "Address",font = ('Times New Roman',10,'bold'),
          fg = 'black').grid(row = 4,column = 0)

''' Data Entry Fields '''

a1 = Entry(reg).grid(row = 0,column = 1)
b1 = Entry(reg).grid(row = 1,column = 1)
c1 = Entry(reg).grid(row = 2,column = 1)
d1 = Entry(reg).grid(row = 3,column = 1)
e1 = Entry(reg).grid(row = 4,column = 1)

def changeText():   #changes text of submit button when clicked
    btn['text'] = 'Submitted'
    
    ''' Submit button '''

btn = Button(reg,text = 'Submit',command = changeText)
btn.grid(row = 5, column = 0)  

#execute
reg.mainloop()