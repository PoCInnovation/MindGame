import os
import torch
import src.train.networks as nn


def ask_network():
    print('Which network do you want to use?')
    print('1 - Focus detection')
    print('2 - Label detection')
    print('3 - Label detection with RNN')

    while True:
        response = input()
        response = int(response) if response.isnumeric() else 0

        if 0 < response < 4:
            break
        print('Invalid input, please enter a following number 1, 2, 3')

    if response == 1:
        return nn.NeuralNetwork()
    if response == 2:
        return nn.LabelNetwork(label_count=4)
    if response == 3:
        return nn.RNNNetwork(label_count=4)
    return None


def load_network():
    network = ask_network()
    filepath = '../models/network.pt'

    if os.path.exists(filepath):
        network.load_state_dict(torch.load(filepath))
        network.eval()
    return network
