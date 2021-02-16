from tkinter import *

root = Tk() 
root.title("Tab Widget") 
tabControl = ttk.Notebook(root)  #Notebook function is used to define tabs

tab1 = Frame(tabControl) 
tab2 = Frame(tabControl) 

#First Tab
tabControl.add(tab1, text = 'Tab 1') 

#Second Tab
tabControl.add(tab2, text = 'Tab 2') 
tabControl.pack(expand = 1, fill = "both") 

lbl1 = Label(tab1, text = "Hello there!").grid(column = 0, row = 0,
                                           padx = 30, pady = 30) 
lbl2 = Label(tab2, text = "General Kenobi").grid(column = 0, row = 0, 
                                             padx = 30, pady = 30) 

root.mainloop() 
