from tkinter import *

root = Tk()
root.title('Scroll Widget')
scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y)

lst = Listbox(root, yscrollcommand = scroll.set)   #listbox() function

#list range for widget
for line in range(1,21):
   lst.insert(END, "This is line number " + str(line))    #insert() function

lst.pack(side = LEFT, fill = BOTH)
scroll.config(command = lst.yview)

root.mainloop()