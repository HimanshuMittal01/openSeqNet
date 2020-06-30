from tkinter import Tk, Label

root = Tk()

# Creating a label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Ny name is Himanshu Mittal!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()

class Node:
    def __init__(self):
        pass

