from tkinter import *

def motion(event):
  print("Mouse position:",event.x, event.y)
  return

master = Tk()
master.title('Mouse Position')
master.geometry('400x300')
move = 'MOVE CURSOR IN WINDOW'
msg = Message(master, text = move)
msg.config(bg = 'lightgreen', font = ('Gothic', 24, 'italic'))

#Bind mouse motion to window
master.bind('<Motion>', motion)
msg.pack()
mainloop()