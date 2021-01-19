from tkinter import *
from tkinter import filedialog

Open = Tk()
Open.title('File Opener')
Open.geometry('200x200')

#Function for opening the file
def file_opener():
   file_input = filedialog.askopenfile(initialdir= "/" )
   print(file_input)
   for i in file_input:
      print(i)
      
#Button to open a file
f = Button(Open, text ='Click to Select a .txt file', command = file_opener)
f.pack()
    
#The file will be view in the console
Open.mainloop()