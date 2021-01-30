from tkinter import *

#second counter function
counter = 0 
def counter_(lbl):
  counter = 0
  def count():
    global counter
    counter += 1
    lbl.config(text = str(counter))
    lbl.after(1000, count)
  count()
 
#Widget window 
root = Tk()
root.title("Seconds Counter")

#Counter display
lbl = Label(root, fg = "crimson")
lbl.pack()
counter_(lbl)

#Close Widget 
btn = Button(root, text = 'Quit', width = 25, command = root.destroy)
btn.pack()

root.mainloop()