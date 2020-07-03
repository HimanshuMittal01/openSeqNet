from .node import Node

class Layer:
    def __init__(self, n, x, canvas):
        '''
        Args:
            n      : Number of nodes in layer
            x      : X-coords of layer
            canvas : Drawing canvas interface
        '''
        self.n = n
        self.x = x
        self.nodes = [None]*n
        self.canvas = canvas
        self._create_nodes()
    
    def _create_nodes(self):
        width  = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        gap = height/self.n
        offset = 5
        for i in range(self.n):
            self.nodes[i] = Node(self.x, offset+gap*i, 2, self.canvas)
    
    def show(self):
        for node in self.nodes:
            node.show()
