import torch

from neuralnetwork import NeuralNetwork, LabelNetwork, RNNNetwork
from os.path import exists


def ask_model():
    print('Which network do you want to use?')
    print('1 - Convolution')
    print('2 - Label detection')
    print('3 - Label detection with RNN')

    while True:
        response = input()
        response = int(response) if response.isnumeric() else 0

        if 0 < response < 4:
            break

    if response == 1:
        return NeuralNetwork()
    if response == 2:
        return LabelNetwork(label_count=4)
    if response == 3:
        return RNNNetwork(label_count=4)
    return None


def load_model():
    model = ask_model()
    filepath = '../models/network.pt'

    if not exists(filepath):
        raise FileNotFoundError('Model training file does not exist (%s)' % filepath)
    model.load_state_dict(torch.load(filepath))
    model.eval()
    return model
