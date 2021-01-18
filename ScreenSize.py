from tkinter import *
base = Tk()
base.title('Screen Size')

#Length and Width of screen in Pixels and mm
length_1 = base.winfo_screenheight()
width_1 = base.winfo_screenwidth()
length_2 = base.winfo_screenmmheight()
width_2 = base.winfo_screenmmwidth()

#Screen Depth
screendepth = base.winfo_screendepth()
print("\n Width x Length (in pixels) = ",'(',width_1, 'x' ,length_1,')')
print("\n Width x Length (in mm) = ", (width_2, length_2))
print("\n Screen depth = ", screendepth)
mainloop()