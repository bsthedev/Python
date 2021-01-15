import tkinter as tk
main = tk.Tk()
main.title('Keyboard Input')
main.geometry('400x300')

str = "Press a Key"

message = tk.Message(main, text = str)
message.config(bg = 'white', font=('Ariel', 28, 'bold'))

#Function to detect button button press on keyboard
def PressAnyKey(label):
   value = label.char1
   print(value)

#Bind function to bind keyboard to program
main.bind('<Key>', lambda i : PressAnyKey(i))

message.pack()
main.mainloop()