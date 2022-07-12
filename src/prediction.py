import torch


def get_prediction(input, model):
    output = model.forward(input, 1)
    _, predicted = torch.max(output.data, 1)
    return predicted
