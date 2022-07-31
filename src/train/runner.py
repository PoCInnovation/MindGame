from src.train.networks import NeuralNetwork
import torch
import matplotlib.pyplot as plt
import src.preprocess as pp
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import numpy as np


def train_network(network, network_type, dataset):
    train_set, test_set = pp.split_data(dataset)
    network, train_accuracies, test_accuracies = train(train_set, test_set, epoch=100, batch_size=32, learning_rate=0.05, network=network)

    plt.plot(train_accuracies)
    plt.plot(test_accuracies)
    torch.save(network.state_dict(), '../models/' + network_type.name + '.pt')
    return network, train_accuracies, test_accuracies


def train(train_set, test_set, epoch, batch_size, learning_rate, network):
    if network is None:
        network = NeuralNetwork()
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=batch_size, shuffle=True)
    # # Load a loss calculator and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(network.parameters(), lr=learning_rate, momentum=0.9)

    train_accuracies = np.zeros(epoch)
    test_accuracies = np.zeros(epoch)

    for iteration in tqdm(range(epoch)):
        average_loss = 0.0

        # Training
        total = 0
        success = 0
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            output = network.forward(inputs, len(inputs))
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
            output = network.forward(inputs, len(inputs))
            _, predicted = torch.max(output.data, 1)
            total += labels.size(0)
            success += (predicted == labels.data).sum()
        test_accuracies[iteration] = 100.0 * success / total
        # -------------------------------------------------------------------

    return network, train_accuracies, test_accuracies
