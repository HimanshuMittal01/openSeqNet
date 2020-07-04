import torch
import matplotlib.colors as mcolors
import matplotlib.cm as cm

class Edge:
    def __init__(self, node1, node2, weight, color, canvas):
        self.node1  = node1
        self.node2  = node2
        self.weight = weight
        self.color  = color
        self.canvas = canvas
    
    def show(self):
        # We can show weight as well if netowrk size is low
        self.canvas.create_line(self.node1.x, self.node1.y, self.node2.x, self.node2.y, fill=self.color)
    
class EdgeMatrix:
    def __init__(self, weights, layer1, layer2, canvas):
        self.weights = weights
        self.layer1 = layer1
        self.layer2 = layer2
        self.canvas = canvas
        self.edges = [[None for i in range(self.layer2.n)] for j in range(self.layer1.n)]

        self._fill()

    def _fill(self):
        maxw = torch.max(self.weights.view(-1,1)).item()
        minw = torch.min(self.weights.view(-1,1)).item()

        norm = mcolors.Normalize(vmin=minw, vmax=maxw, clip=True)
        mapper = cm.ScalarMappable(norm=norm, cmap=cm.Set1)
         
        for i in range(self.layer1.n):
            for j in range(self.layer2.n):
                self.edges[i][j] = Edge(
                    self.layer1.nodes[i],
                    self.layer2.nodes[j],
                    self.weights[j][i],
                    mcolors.to_hex(mapper.to_rgba(self.weights[j][i].detach().numpy())),
                    self.canvas
                    )
    
    def show(self):
        for i in range(self.layer1.n):
            for j in range(self.layer2.n):
                self.edges[i][j].show()