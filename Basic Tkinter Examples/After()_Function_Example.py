import random
from tkinter import *

base = Tk()

a = Label(base, text= "After() Function")
a.pack()

main = Frame(base, width=450, height=500)
main.pack()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat','Sun']

#Display the days randomly one after another
def weekdays():
   if not days:
     return
   rand = random.choice(days)
   frame = Label(main, text = rand)
   frame.pack()
   main.after(1000, weekdays)   #1 second delay after each day
   days.remove(rand)

base.after(0, weekdays)
base.mainloop()