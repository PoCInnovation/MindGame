from neuralnetwork import NeuralNetwork
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import numpy as np

LEARNING_RATE = 0.05
EPOCH = 100
BATCH_SIZE = 64

def train_network(train_set, test_set):

    network = NeuralNetwork()
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=True)
    # # Load a loss calculator and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(network.parameters(), lr=LEARNING_RATE, momentum=0.9)

    iteration = 0

    train_accuracies = np.zeros(EPOCH)
    test_accuracies = np.zeros(EPOCH)

    for iteration in tqdm(range(EPOCH)):
        average_loss = 0.0

        # Training
        total = 0
        success = 0
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            try:
                output = network.forward(inputs, BATCH_SIZE)
            except:
                continue
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
            average_loss += loss.item()
            _, predicted = torch.max(output.data, 1)
            total += labels.size(0)
            success += (predicted == labels.data).sum()
        train_accuracies[iteration] = 100.0 * success / total
        # -------------------------------------------------------------------

        # Testing
        total = 0
        success = 0
        for inputs, labels in test_loader:
            try:
                output = network.forward(inputs, BATCH_SIZE)
            except:
                continue
            _, predicted = torch.max(output.data, 1)
            total += labels.size(0)
            success += (predicted == labels.data).sum()
        test_accuracies[iteration] = 100.0 * success / total
        # -------------------------------------------------------------------
    return network, train_accuracies, test_accuracies