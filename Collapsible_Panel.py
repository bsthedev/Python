from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

#class for collapsible panel
class col_pane(ttk.Frame):
   def __init__(self, MainWindow, expanded_text, collapsed_text):
      ttk.Frame.__init__(self, MainWindow)
      self.MainWindow = MainWindow
      self._expanded_text = expanded_text
      self._collapsed_text = collapsed_text
      self.columnconfigure(1, weight=1)
      self._variable = tk.IntVar()
      
      # Creating Checkbutton
      self._button = ttk.Checkbutton(self, variable=self._variable,
      command=self._activate, style="TButton")
      self._button.grid(row=0, column=0)
      
      # Create a Horizontal line along button
      self._separator = ttk.Separator(self, orient="horizontal")
      self._separator.grid(row=0, column=1, sticky="we")
      self.frame = ttk.Frame(self)
      
      # Activate the class
      self._activate()
      
   def _activate(self):
      if not self._variable.get():
         # Remove this widget when button pressed
         self.frame.grid_forget()
         # Shows collapsed text
         self._button.configure(text=self._collapsed_text)
      elif self._variable.get():
         self.frame.grid(row=1, column=0, columnspan=2)
         self._button.configure(text=self._expanded_text)
   def toggle(self):
      self._variable.set(not self._variable.get())
      self._activate()


root = Tk()
root.geometry('400x300')

#Creating Object of Collapsible Pane
col_pane_obj = col_pane(root, 'Close Panel', 'Open Panel')
col_pane_obj.grid(row=0, column=0)

#Creating Collapsible panel contents
b = Button(col_pane_obj.frame, text = "Hello Comrade").grid(
    row=1, column=2, pady=20)
b = Checkbutton(col_pane_obj.frame, text = "This is a Collapsible Panel....!!!").grid(
    row=3, column=4, pady=20)
mainloop()