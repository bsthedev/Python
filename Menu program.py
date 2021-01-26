from tkinter import *

#command function for each option
def example():
   file = Toplevel(root)
   btn = Button(file, text = "Just Example")
   btn.pack()
   
root = Tk()
root.title('MENU')

#Menu options
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "New", command = example)
filemenu.add_command(label = "Open", command = example)
filemenu.add_command(label = "Save", command = example)
filemenu.add_command(label = "Save as...", command = example)
filemenu.add_command(label = "Close", command = example)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)  #adds option to fmenu
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label = "Undo", command = example)
editmenu.add_separator()
editmenu.add_command(label = "Cut", command = example)
editmenu.add_command(label = "Copy", command = example)
editmenu.add_command(label = "Paste", command = example)
editmenu.add_command(label = "Delete", command = example)
editmenu.add_command(label = "Select All", command = example)
menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = example)
helpmenu.add_command(label = "About...", command = example)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)
root.mainloop()