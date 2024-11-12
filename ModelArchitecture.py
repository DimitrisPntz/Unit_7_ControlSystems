import torch
import torch.nn as nn

# Define the Model Architecture
class NumberIdentifier(nn.Module):
    def __init__(self):
        super().__init__()

        self.Identifier = nn.Sequential(
            # Our Input Features are 28 x 28 so 784 
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10) # We have 10 digits to identify from 0 -> 9 so we have ten output classes
        )

    def forward(self, x):
        # Flatten x so it isn't a 28 x 28 and a 1D 784 image
        x = x.view(x.size(0), -1)
        return self.Identifier(x)
    
    def predict(self, x):
        x = x.view(x.size(0), -1)
        return torch.argmax(self.Identifier(x))