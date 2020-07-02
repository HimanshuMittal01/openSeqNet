import os
from tkinter import *
from tkinter import filedialog
from src.layer import Layer
import torch

root = Tk()
canvas = Canvas(root,bg="white",height=600,width=600)
canvas.pack()

def openfile():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a file')
    if len(tempdir) > 0:
        print("You chose %s" % tempdir)

button = Button(root, padx=50, text="Click me!!", command=openfile)
button.pack()

root.update()
layer = Layer(50, canvas)
layer.show()

root.mainloop()

# if __name__=='__main__':
    
#     root.mainloop()
