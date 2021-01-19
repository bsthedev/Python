''' This program will save any type of empty file to system storage
    The file type extension (Ex: .txt, .docx, etc) needs to be defined 
    after saving '''

from tkinter import *
from tkinter.filedialog import asksaveasfile

Save = Tk()
Save.title('Save a File')
Save.geometry('200x200')

#Function to save file
def SaveFile():
   data = [('All tyes(*_*)', '*_*')]
   file = asksaveasfile(filetypes = data, defaultextension = data)

btn = Button(Save, text = 'Click to save file ', bd = 5 ,command = SaveFile)
btn.pack()

#Saves an empty file
Save.mainloop()