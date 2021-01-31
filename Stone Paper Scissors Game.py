import random
from tkinter import *

window = Tk()
window.title('Stone Paper Scissors')
window.geometry('400x300')

USER_SCORE = 0
CPU_SCORE = 0
USER_CHOICE = " "
CPU_CHOICE = " " 

#Function to convert number to choice
def choice_to_number(choice):
    game = {'stone':0,'paper':1,'scissor':2}
    return game[choice]

#Function to convert choice to number
def number_to_choice(number):
    game = {0:'stone',1:'paper',2:'scissor'}
    return game[number]

#Function for Random computer choice
def random_computer_choice():
    return random.choice(['stone','paper','scissor']) 

#Function to display result
def result(my_choice,cpu_choice):
    global USER_SCORE
    global CPU_SCORE
    user = choice_to_number(my_choice)
    cpu = choice_to_number(cpu_choice)
    if(user == cpu):
        print("Tie")
    elif((user - cpu) % 3 == 1):
        print("You win")
        USER_SCORE += 1
    else:
        print("CPU wins")
        CPU_SCORE += 1
    text_area = Text(window, height = 12 ,width = 30, bg = "yellow")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \nMy Score : {us} \nComputer Score : {cs} ".format(uc=USER_CHOICE,cc=CPU_CHOICE,us=USER_SCORE,cs=CPU_SCORE)    
    text_area.insert(END,answer)
   
#Functions for Stone, Paper & Scissor         
def stone():
    global USER_CHOICE
    global CPU_CHOICE
    USER_CHOICE = 'stone'
    CPU_CHOICE = random_computer_choice()
    result(USER_CHOICE,CPU_CHOICE)
def paper():
    global USER_CHOICE
    global CPU_CHOICE
    USER_CHOICE = 'paper'
    CPU_CHOICE = random_computer_choice()
    result(USER_CHOICE,CPU_CHOICE)
def scissor():
    global USER_CHOICE
    global CPU_CHOICE
    USER_CHOICE = 'scissor'
    CPU_CHOICE=random_computer_choice() 
    result(USER_CHOICE,CPU_CHOICE)

#Buttons to select Stone, Paper & Scissors
button1 = Button(text="     Rock     ",bg = "sky blue",
                 command = stone).grid(column = 1,row = 1)
button2 = Button(text="     Paper    ",bg = "pink",
                 command = paper).grid(column = 1,row = 2)
button3 = Button(text="    Scissor   ",bg = "magenta",
                 command = scissor).grid(column = 1,row = 3)

window.mainloop()
