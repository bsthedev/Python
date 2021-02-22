## PyQt :-

_PyQt is a toolkit for graphical user interface (GUI) widgets.
PyQt is the product of the combination of the Python language and the Qt library. PyQt is coming with the Qt Builder. 
We will use it to get the python code from the Qt Creator. With the support of a qt designer, we can build a GUI, and then we can get python code for that GUI.
PyQt supports all platforms including Windows, macOS and UNIX. PyQt can be used to create stylish GUIs, a modern and portable python framework._

## Advantages of using PyQt -
* Coding versatility : GUI programming with Qt is built around the idea of signals and slots for creating contact between objects. 
   This allows versatility in dealing with GUI incidents which results in a smoother code base.
* More than a framework : Qt uses a broad variety of native platform APIs for networking, database development, and more. It provides primary access to them through a special API.
* Various UI components : Qt provides multiple widgets, such as buttons or menus, all designed with a basic interface for all compatible platforms.
* Various learning resources : As PyQt is one of the most commonly used UI systems for Python, you can conveniently access a broad variety of documentation.

## Disadvantages of using PyQt -
*  Lack of Python-specific documentation for classes in PyQt5
* It takes a lot of time to grasp all the specifics of PyQt, meaning it’s a pretty steep learning curve.
* If the application is not open-source, you must pay for a commercial license.

## Syntax Example -

import sys

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QWidget 

app = QApplication(sys.argv)

root = QWidget()   
root.setWindowTitle('Example')  
root.move(60, 15)  
txt = QLabel('Example', parent = root)  
txt.move(60, 15)

root.show() 

sys.exit(app.exec_())




## Tkinter :-

_Tkinter is an open-source Python Graphic User Interface (GUI) library well known for its simplicity. It comes pre-installed in Python.
These characteristics make it a strong position for beginners and intermediates to begin with. Tkinter cannot be used for larger-scale projects._

## Advantages of using Tkinter -
* Tkinter is easy and fast to implement as compared to any other GUI toolkit.
* Tkinter is more flexible and stable.
* Tkinter is included in Python, so nothing extra need to download.
* Tkinter provides a simple syntax.
* Tkinter is really easy to understand and master.
* Tkinter provides three geometry managers : place, pack, and grid. That is much more powerful and easy to use.

## Disadvantages of using Tkinter -
* Tkinter does not include advanced widgets.
* It has no similar tool as Qt Designer for Tkinter.
* It doesn’t have a reliable UI.
* Sometime, it is hard to debug in Tkinter.

## Syntax -

import tkinter as tk 

root = tk.Tk() 

txt = tk.Label(root, text="Welcome to GeekForGeeks") 

txt.pack() 

root.mainloop() 
