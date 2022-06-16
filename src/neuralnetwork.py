import torch.nn as nn
import torch.nn.functional as F

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()

        # Convolution layer
        self.conv1 = nn.Conv1d(1, 6, 5)
        self.conv2 = nn.Conv1d(6, 16, 5)
        self.max_pool = nn.MaxPool1d(2)
        # --------------------------------

        self.dropout = nn.Dropout(0.25)

        # Fully connected layer
        self.linear1 = nn.Linear(16 * 5, 120)
        self.linear2 = nn.Linear(120, 2)
        # --------------------------------

    def forward(self, x, batch_size):
        x = x.view(batch_size, 1, 32)
        # Convolution layer
        x = F.tanh(self.conv1(x))
        x = self.max_pool(x)
        x = F.tanh(self.conv2(x))
        x = self.max_pool(x)
        # -----------------------

        x = self.dropout(x)

        # Flatten filters
        x = x.view(-1, 16 * 5)

        # Fully connected layer
        x = F.tanh(self.linear1(x))
        x = F.tanh(self.linear2(x))
        # -------------------------
        return x