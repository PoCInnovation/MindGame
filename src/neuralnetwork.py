import torch
import torch.nn as nn


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
        x = torch.tanh(self.conv1(x))
        x = self.max_pool(x)
        x = torch.tanh(self.conv2(x))
        x = self.max_pool(x)
        # -----------------------

        x = self.dropout(x)

        # Flatten filters
        x = x.view(-1, 16 * 5)

        # Fully connected layer
        x = torch.tanh(self.linear1(x))
        x = torch.tanh(self.linear2(x))
        # -------------------------
        return x


class LabelNetwork(nn.Module):
    def __init__(self, label_count):
        super(LabelNetwork, self).__init__()

        self.label_count = label_count

        # Convolution layer
        self.conv1 = nn.Conv1d(1, 6, 5)
        self.conv2 = nn.Conv1d(6, 16, 5)
        self.max_pool = nn.MaxPool1d(2)
        # --------------------------------

        self.dropout = nn.Dropout(0.25)

        # Fully connected layer
        self.linear1 = nn.Linear(16 * 5, 120)
        self.linear2 = nn.Linear(120, label_count)
        # --------------------------------

    def forward(self, x, batch_size):
        x = x.view(batch_size, 1, 32)
        # Convolution layer
        x = torch.tanh(self.conv1(x))
        x = self.max_pool(x)
        x = torch.tanh(self.conv2(x))
        x = self.max_pool(x)
        # -----------------------

        x = self.dropout(x)

        # Flatten filters
        x = x.view(-1, 16 * 5)

        # Fully connected layer
        x = torch.tanh(self.linear1(x))
        x = torch.tanh(self.linear2(x))
        # -------------------------
        return x


class RNNNetwork(nn.Module):
    def __init__(self, label_count):
        super(RNNNetwork, self).__init__()

        self.label_count = label_count

        # Convolution layer
        self.conv1 = nn.Conv1d(1, 6, 5)
        self.conv2 = nn.Conv1d(6, 16, 5)
        self.max_pool = nn.MaxPool1d(2)
        # --------------------------------

        self.dropout = nn.Dropout(0.25)

        # Fully connected layer
        self.linear1 = nn.Linear(16 * 5, 120)
        self.linear2 = nn.Linear(120, label_count)
        # --------------------------------

    def forward(self, x, batch_size):
        x = x.view(batch_size, 1, 32)
        # Convolution layer
        x = torch.tanh(self.conv1(x))
        x = self.max_pool(x)
        x = torch.tanh(self.conv2(x))
        x = self.max_pool(x)
        # -----------------------

        x = self.dropout(x)

        # Flatten filters
        x = x.view(-1, 16 * 5)

        # Fully connected layer
        x = torch.tanh(self.linear1(x))
        x = torch.tanh(self.linear2(x))
        # -------------------------
        return x
