import json

import numpy as np
from teenygrad.tensor import Tensor
from teenygrad.nn import optim

class Model:
  def __init__(self):
    self.w = Tensor.randn(1)
    self.w.requires_grad = True
    self.b = Tensor.zeros(1)
    self.b.requires_grad = True 
  def __call__(self, x:Tensor):
    return x@self.w + self.b
    

    
def run(post_data):
        try:
            json_data = json.loads(post_data)
            response_message = f"Received JSON data: {json_data}"
            x1 = json_data['x1']
            x2 = json_data['x2']
            
            # list concatenation
            x = Tensor(x1+x2).reshape([-1, 1])
            # making labels
            y = Tensor([0]*len(x1) + [1] * len(x2))
            model = Model()
            
   
            # setting SGD with quite aggressive learning rate
            opt = optim.SGD([model.w, model.b], lr=1.0)
               
            # setting SGD with quite aggressive learning rate
            opt = optim.SGD([model.w, model.b], lr=1.0)
            criterion = Tensor.binary_crossentropy_logits

            # running optimization for 1000 epochs
            for _ in range(1000):
                opt.zero_grad()
                loss = criterion(model(x), y)
                loss.backward()
                opt.step()
            
            input_ = json_data['input']
            response_message =  str(model(Tensor([input_])).sigmoid().numpy())
            
        except Exception as e:
             response_message = repr(e)
        return response_message
        
