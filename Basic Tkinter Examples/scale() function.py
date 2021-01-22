from tkinter import *

#Slider value function
def sel():
   val = "Value = " + str(var.get())
   lbl.config(text = val)

root = Tk()
root.title('Slider Widget')
var = DoubleVar()

#Scale provides a slider
slide = Scale(root, variable = var)
slide.pack(anchor = CENTER)

btn = Button(root, text = "Slider Value", command = sel)
btn.pack(anchor = CENTER)

lbl = Label(root)
lbl.pack()

root.mainloop()