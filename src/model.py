import os
import torch
import src.train.networks as nn

from enum import Enum


class NetworkType(Enum):
    FOCUS = 0
    LABEL = 1
    LABEL_RNN = 2
    LABEL_LINEAR = 3
    LINEAR = 4


def ask_network():
    print('Which network do you want to use?')
    print('1 - Focus detection with CNN')
    print('2 - Label detection with CNN')
    print('3 - Label detection with RNN')
    print('4 - Label detection with Linear Network')
    print('5 - Focus detection with Linear Network')

    while True:
        response = input()
        response = int(response) if response.isnumeric() else 0

        if 0 < response <= 5:
            break
        print('Invalid input, please enter a following number 1, 2, 3, 4, 5')

    response -= 1
    if response == NetworkType.FOCUS.value:
        return nn.NeuralNetwork(), NetworkType.FOCUS
    if response == NetworkType.LABEL.value:
        return nn.LabelNetwork(label_count=4), NetworkType.LABEL
    if response == NetworkType.LABEL_RNN.value:
        return nn.RNNNetwork(label_count=4), NetworkType.LABEL_RNN
    if response == NetworkType.LABEL_LINEAR.value:
        return nn.LinearClassifierNetwork(label_count=4), NetworkType.LABEL_LINEAR
    if response == NetworkType.LINEAR.value:
        return nn.LinearClassifierNetwork(label_count=2), NetworkType.LINEAR
    return None, None


def load_network():
    network, network_type = ask_network()
    filepath = '../models/' + network_type.name + '.pt'

    if os.path.exists(filepath):
        network.load_state_dict(torch.load(filepath))
        network.eval()
    return network, network_type
