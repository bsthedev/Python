from tkinter import *
from PIL import ImageTk ,Image

base = Tk()
base.title('Image Button')

img = ImageTk.PhotoImage(Image.open("D:\\button.jpg"))
lab = Label(image=img)
lab.pack()

def close_window(): 
    base.destroy()

button = Button(base, text='Quit', bd = 5,
                fg = 'blue', command = close_window)
button.pack()
base.mainloop()