from tkinter import Tk, Canvas
from src import node

root = Tk()
canvas = Canvas(root,bg="white",height=300,width=300)
canvas.pack()

node = node.Node(50,50,20,canvas)
node.show()

if __name__=='__main__':
    root.mainloop()
