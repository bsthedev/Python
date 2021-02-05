from tkinter import * 
import random 
  
#colour list 
colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange',
           'White','Purple','Brown','Crimson'] 
score = 0
  
#game time 
timeleft = 30
  
#game start function
def startGame(event): 
      
    if timeleft == 30:  
        countdown() 
    #Picks next colour
    nextColour() 
  
#Function to choose and display the next colour
def nextColour(): 
    global score 
    global timeleft 
    if timeleft > 0: 
        e.focus_set() 
  
        #if the colour typed is equal to the colour of the text 
        if e.get().lower() == colours[1].lower(): 
                 score += 1
        e.delete(0, END) 
        
        random.shuffle(colours) 
          
        #Change the colour of the text
        label.config(fg = str(colours[1]), text = str(colours[0])) 
        scoreLabel.config(text = "Score: " + str(score)) 
  
  
#Countdown timer function  
def countdown(): 
    global timeleft 
    if timeleft > 0: 
        timeleft -= 1
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
        timeLabel.after(1000, countdown) 
 
#Widget Window
root = Tk()
root.title("COLOUR GAME") 
root.geometry("400x300") 
  
#Instructions label 
instructions = Label(root, text = "Type the colour of the words!!!",
                     font = ('Gothix', 12)) 
instructions.pack()  
  
#Score label 
scoreLabel = Label(root, text = "Press enter to start",
                           font = ('Helvetica', 12)) 
scoreLabel.pack() 
  
#Time left label 
timeLabel = Label(root, text = "Time left: " + str(timeleft),
                          font = ('Gothic', 12)) 
                
timeLabel.pack() 
  
#Display the colours 
label = Label(root, font = ('Helvetica', 60)) 
label.pack() 

e = Entry(root) 
 
#When the enter key is pressed start game
root.bind('<Return>', startGame) 
e.pack() 
e.focus_set() 

#Start the program
root.mainloop() 
