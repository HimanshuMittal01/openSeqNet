import torch
from .layer import Layer

class ModelManager:
    def __init__(self, filepath, canvas):
        self.filepath = filepath
        self.canvas = canvas
        self.model = self._load_torch_model(filepath)
        self.layers = []

        # Instantiates graph structure
        self._create_graph()
    
    def _load_torch_model(self, filepath):
        '''Loads pytorch model
        '''
        # TODO : Handle errors
        return torch.load(filepath)
    
    def _create_graph(self):
        for name,param in self.model.named_parameters():
            if (name.endswith(".bias")):
                continue
            self.layers.append(param.size()[0]) # 0 index gives output dims and 1 will give input dims
    
    def get_num_layers(self):
        '''Returns number of layers
        '''
        pass
    def show(self):
        '''Shows the model on canvas
        '''
        width  = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        x = 10
        for layer_size in self.layers:
            layer = Layer(layer_size, x, self.canvas)
            layer.show()
            x += 10
        
