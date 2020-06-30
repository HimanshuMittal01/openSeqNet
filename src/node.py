from .util import create_circle

class Node:
    def __init__(self,x,y,r,canvas):
        self.x = x
        self.y = y
        self.r = r
        self.canvas = canvas

    def show(self):
        create_circle(self.x, self.y, self.r, self.canvas)