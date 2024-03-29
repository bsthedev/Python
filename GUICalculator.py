from tkinter import *

''' Button Commands '''

expression = ""
def input_number(number, equation):
   global expression
   expression = expression + str(number)
   equation.set(expression)
def clear_input_field(equation):
   global expression
   expression = ""
   equation.set("  ")
def evaluate(equation):
  global expression
  try:
    result = str(eval(expression))
    equation.set(result)
    expression = ""
  except:
   expression = ""
   
   ''' Calculator GUI Code '''
   
def main():
   window = Tk()
   window.title("Calculator")
   window.geometry("400x300")
   equation = StringVar()
   input_field = Entry(window, textvariable=equation)
   input_field.place(height=100)
   input_field.grid(columnspan=5, ipadx=100, ipady=5)
   equation.set("   ")
   
   ''' Buttons '''
   
   B1 = Button(window, text='1', fg='white', bg='black', bd=0, command=lambda: input_number(1, equation), height=2, width=7)
   B1.grid(row=2, column=0)
   B2 = Button(window, text='2', fg='white', bg='black', bd=0, command=lambda: input_number(2, equation), height=2, width=7)
   B2.grid(row=2, column=1)
   B3 = Button(window, text='3', fg='white', bg='black', bd=0, command=lambda: input_number(3, equation), height=2, width=7)
   B3.grid(row=2, column=2)
   B4 = Button(window, text='4', fg='white', bg='black', bd=0, command=lambda: input_number(4, equation), height=2, width=7)
   B4.grid(row=3, column=0)
   B5 = Button(window, text='5', fg='white', bg='black', bd=0, command=lambda: input_number(5, equation), height=2, width=7)
   B5.grid(row=3, column=1)
   B6 = Button(window, text='6', fg='white', bg='black', bd=0, command=lambda: input_number(6, equation), height=2, width=7)
   B6.grid(row=3, column=2)
   B7 = Button(window, text='7', fg='white', bg='black', bd=0, command=lambda: input_number(7, equation), height=2, width=7)
   B7.grid(row=4, column=0)
   B8 = Button(window, text='8', fg='white', bg='black', bd=0, command=lambda: input_number(8, equation), height=2, width=7)
   B8.grid(row=4, column=1)
   B9 = Button(window, text='9', fg='white', bg='black', bd=0, command=lambda: input_number(9, equation), height=2, width=7)
   B9.grid(row=4, column=2)
   B0 = Button(window, text='0', fg='white', bg='black', bd=0, command=lambda: input_number(0, equation), height=2, width=7)
   B0.grid(row=5, column=0)
   Bplus = Button(window, text='+', fg='white', bg='black', bd=0, command=lambda: input_number('+', equation), height=2, width=7)
   Bplus.grid(row=2, column=3)
   Bminus = Button(window, text='-', fg='white', bg='black', bd=0, command=lambda: input_number('-', equation), height=2, width=7)
   Bminus.grid(row=3, column=3)
   Bmultiply = Button(window, text='*', fg='white', bg='black', bd=0, command=lambda: input_number('*', equation), height=2, width=7)
   Bmultiply.grid(row=4, column=3)
   Bdivide = Button(window, text='/', fg='white', bg='black', bd=0, command=lambda: input_number('/', equation), height=2, width=7)
   Bdivide.grid(row=5, column=3)
   Bequal = Button(window, text='=', fg='white', bg='black', bd=0, command=lambda: evaluate(equation), height=2, width=7)
   Bequal.grid(row=5, column=2)
   Bclear = Button(window, text='Clear', fg='white', bg='black', bd=0, command=lambda: clear_input_field(equation), height=2, width=7)
   Bclear.grid(row=5, column=1)
   Bpow = Button(window, text='^', fg='white', bg='black', bd=0, command=lambda: input_number('**', equation), height=2, width=7)
   Bpow.grid(row=6, column=3)
   window.mainloop()
   
   '''start of the program'''
   
if __name__ == '__main__':
      main()
