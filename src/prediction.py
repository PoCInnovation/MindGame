import torch


def get_prediction(x, model):
    output = model.forward(x, 1)
    _, predicted = torch.max(output.data, 1)
    return predicted
