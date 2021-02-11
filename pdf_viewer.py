from tkinter import*
from tkPDFViewer import tkPDFViewer as pdf 

root = Tk() 
root.title('PDF Viewer')
root.geometry("500x750") 
  
#creating object of ShowPdf 
v1 = pdf.ShowPdf() 
  
#Adding pdf location and width and height.
v2 = v1.pdf_view(root, pdf_location = r"Add pdf location here",
                 width = 50, height = 100).pack() 

root.mainloop()