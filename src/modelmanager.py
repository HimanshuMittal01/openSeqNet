import torch
from .layer import Layer
from .edge import EdgeMatrix

class ModelManager:
    def __init__(self, filepath, canvas):
        self.filepath = filepath
        self.canvas = canvas
        self.model = self._load_torch_model(filepath)
        self.layers = []
        self.weights = []

        # Instantiates graph structure
        self.num_layers = self.get_num_layers()
        self._create_graph()
    
    def _load_torch_model(self, filepath):
        '''Loads pytorch model
        '''
        # TODO : Handle errors
        return torch.load(filepath)
    
    def _create_graph(self):
        '''Creates necessary data structures for graph
        '''
        width  = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # TODO: This is not the right thing, collisions may happen
        gap = width/self.num_layers 
        offset = gap/2

        num_layer = 0
        for name,param in self.model.named_parameters():
            if (name.endswith(".bias")):
                continue
            if (num_layer==0):
                self.layers.append(Layer(param.size()[1], offset+gap*num_layer, self.canvas))
            num_layer += 1
            self.layers.append(Layer(param.size()[0], offset+gap*num_layer, self.canvas))
            self.weights.append(EdgeMatrix(param, self.layers[num_layer-1], self.layers[num_layer], self.canvas))
    
    def get_num_layers(self):
        '''Returns number of layers
        '''
        num_layers = 1 # For input layer
        for name,param in self.model.named_parameters():
            if (name.endswith(".bias")):
                continue
            num_layers+=1
        
        return num_layers
    def update(self):
        '''Updates the x and y location of the layers
        '''
        pass
    def show(self):
        '''Shows the model on canvas
        '''
        for layer in self.layers:
            layer.show()
        for edges in self.weights:
            edges.show()