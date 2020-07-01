from tkinter import *
from src.layer import Layer

root = Tk()
canvas = Canvas(root,bg="white",height=600,width=600)
canvas.pack()

root.update()
layer = Layer(50, canvas)
layer.show()

if __name__=='__main__':
    root.mainloop()
