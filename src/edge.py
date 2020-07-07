import torch
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from .util import hex_to_rgb, storage
from PIL import Image, ImageDraw, ImageTk

class Edge:
    count = 0
    def __init__(self, node1, node2, weight, color, canvas):
        self.node1  = node1
        self.node2  = node2
        self.weight = weight
        self.color  = color
        self.canvas = canvas

        self.id = Edge.count
        Edge.count += 1
    
    def _create_line(self, x1, y1, x2, y2, canvas, **kwargs):
        x1,x2,y1,y2 = int(abs(x1)),int(abs(x2)),int(abs(y1)),int(abs(y2))
        x,y = min(x1,x2), min(y1,y2)
        w,h = max(x1,x2)-x, max(y1,y2)-y
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha')*255)
            fill  = kwargs.pop('fill')
            fill  = hex_to_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (w,h))
            ImageDraw.Draw(image).line([(x1-x,y1-y),(x2-x,y2-y)], fill=fill,width = 1)
            storage.append(ImageTk.PhotoImage(image))
            canvas.create_image(x,y, image=storage[-1], anchor='nw')
    
    def show(self):
        # We can show weight as well if netowrk size is low
        self._create_line(self.node1.x, self.node1.y, self.node2.x, self.node2.y, self.canvas, fill=self.color, alpha=.8)
        # self.canvas.create_line(self.node1.x, self.node1.y, self.node2.x, self.node2.y, fill=self.color)
    
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
        mapper = cm.ScalarMappable(norm=norm, cmap=cm.YlOrRd) # Set 1
         
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
        values,_ = self.weights.view(-1).topk(10)
        values = values.tolist()
        print(values)
        for i in range(self.layer1.n):
            for j in range(self.layer2.n):
                if self.edges[i][j].weight in values:
                    self.edges[i][j].show()