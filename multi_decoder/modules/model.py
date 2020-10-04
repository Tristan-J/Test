import torch
from torch import nn
import numpy as np

def f(x):
    return x+x

class myModel(nn.Module):
    def __init__(self):
        super(myModel, self).__init__()
        self.encoder = nn.ModuleList()
        self.encoder.append(nn.Conv1d(1,1,kernel_size=2))

        self.decoder_1 = nn.ModuleList()
        self.decoder_1.append(nn.Conv1d(1,1,kernel_size=2))
        
        self.decoder_2 = nn.ModuleList()
        self.decoder_2.append(nn.Conv1d(1,1,kernel_size=2))
    def forward(self, x, decoder_idx):
        for f in self.encoder:
            x = f(x)
        if idx == 1:
            for f in self.decoder_1:
                x = f(x)
        elif idx == 2:
            for f in self.decoder_2:
                x = f(x)
                x = f(x)
        return x

model = myModel()

x = torch.array([10])

optimizer = 

out = model(x, 1)
optimizer.zero_grad()
loss.backward()
optimizer.step()

out = model(x, 2)
optimizer.zero_grad()
loss.backward()
optimizer.step()