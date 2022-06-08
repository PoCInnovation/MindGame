import torch

def get_prediction(index, dataset, model):
    input = dataset[index][0]
    output = model.forward(input, 1)
    _, predicted = torch.max(output.data, 1)
    return predicted