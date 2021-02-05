from tkinter import *
  
#Create Tkinter window 
frame = Tk() 
frame.title('Cursor Types') 
frame.geometry('200x200') 

#Cursor type plus on widget
frame.config(cursor = "plus")

#Xterm type cursor on Text  
L1 = Label(frame, text= "Text", cursor = "xterm").pack() 

#Circle type cursor on Circle button 
B1 = Button(frame, text = "Circle Cursor", cursor = "circle").pack() 

#Heart type cursor on Plus button  
B2 = Button(frame, text = "Heart cursor", cursor = "heart").pack() 

#Dot type cursor on Exit button  
a = Button(frame, text = 'Exit', cursor = "dot", 
              command = frame.destroy).pack() 

''' Different Cursor types can be arrow, circle, clock, cross, dotbox, exchange, fleur, heart, man, mouse,
    pirate, plus, shuttle, sizing, spider, spraycan, star, targe, tcross, trek and watch '''
  
frame.mainloop() 
