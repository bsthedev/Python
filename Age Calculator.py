import datetime
from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Age Calculator App")

name = Label(text = "Name").grid(column = 0,row = 1)
year = Label(text = "Year").grid(column = 0,row = 2)
month = Label(text = "Month").grid(column = 0,row = 3)
date = Label(text = "Day").grid(column = 0,row = 4)

nameEntry = Entry()
nameEntry.grid(column=1,row=1)
yearEntry = Entry()
yearEntry.grid(column=1,row=2)
monthEntry = Entry()
monthEntry.grid(column=1,row=3)
dateEntry = Entry()
dateEntry.grid(column=1,row=4)

def getInput():
    name = nameEntry.get()
    yn = Person(name,datetime.date(int(yearEntry.get()),
                                   int(monthEntry.get()),
                                   int(dateEntry.get())))
    
    textArea = Text(window, height = 10,width = 25)
    textArea.grid(column = 1,row = 6)
    answer = " {yn}, You are {age} years old!!! ".format(yn = name, age = yn.age())
    textArea.insert(END, answer)

button = Button(window, text = "Calculate Age", bg = 'red', command = getInput)
button.grid(column = 1,row = 5)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


window.mainloop()