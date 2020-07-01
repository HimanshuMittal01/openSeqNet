from .node import Node

class Layer:
    def __init__(self, n, canvas):
        self.n = n
        self.nodes = [None]*n
        self.canvas = canvas
        self._create_nodes()
    
    def _create_nodes(self):
        width  = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        gap = height/self.n
        offset = 5
        for i in range(self.n):
            self.nodes[i] = Node(10, offset+gap*i, 2, self.canvas)
    
    def show(self):
        for node in self.nodes:
            node.show()
