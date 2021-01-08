from tkinter import * 
from tkinter.ttk import *
ab = Tk() 
''' determinate mode, i.e; bar moves from beginning to end '''

pbar = Progressbar(ab, orient = HORIZONTAL, length = 100, mode = 'determinate') 
  
''' bar animation with time period of 0.5s'''

def bar(): 
    import time 
    pbar['value'] = 20
    ab.update_idletasks() 
    time.sleep(0.5) 
  
    pbar['value'] = 40
    ab.update_idletasks() 
    time.sleep(0.5) 
  
    pbar['value'] = 50
    ab.update_idletasks() 
    time.sleep(0.5) 
  
    pbar['value'] = 60
    ab.update_idletasks() 
    time.sleep(0.5) 
  
    pbar['value'] = 80
    ab.update_idletasks() 
    time.sleep(0.5)
    
    pbar['value'] = 100
    
    ''' Finish button which appears after progress reaches 100, this button 
    closes the window '''
    
    def close_window(): 
        ab.destroy()
    
    des = Button(ab, text = 'Finish', command = close_window)
    des.pack()
    
''' Progress start button ''' 
  
pbar.pack(pady = 10) 
Button(ab, text = 'Start', command = bar).pack(pady = 10) 

#execute 
ab.mainloop()