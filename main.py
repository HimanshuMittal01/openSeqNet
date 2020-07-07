import os
from tkinter import *
from tkinter import filedialog
from src.modelmanager import ModelManager
import torch

root = Tk()
root.title("OpenSeqNet")
canvas = Canvas(root,bg="white",height=600,width=1000)
canvas.pack()

model_filepath = None
def openfile():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a file')
    if len(tempdir) > 0:
        print("You chose %s" % tempdir)
        model_filepath = tempdir
        manager = ModelManager(model_filepath, canvas)
        manager.show()

button = Button(root, padx=50, text="Click me!!", command=openfile)
button.pack()

root.update()


root.mainloop()

# if __name__=='__main__':
    
#     root.mainloop()
