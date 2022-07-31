import os
import torch
import src.train.networks as nn

from enum import Enum


class NetworkType(Enum):
    FOCUS = 0
    LABEL = 1
    LABEL_RNN = 2


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

    response -= 1
    if response == NetworkType.FOCUS.value:
        return nn.NeuralNetwork(), NetworkType.FOCUS
    if response == NetworkType.LABEL.value:
        return nn.LabelNetwork(label_count=4), NetworkType.LABEL
    if response == NetworkType.LABEL_RNN.value:
        return nn.RNNNetwork(label_count=4), NetworkType.LABEL_RNN
    return None, None


def load_network():
    network, network_type = ask_network()
    filepath = '../models/' + network_type.name + '.pt'

    if os.path.exists(filepath):
        network.load_state_dict(torch.load(filepath))
        network.eval()
    return network, network_type
