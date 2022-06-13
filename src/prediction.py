import torch

def get_prediction(sample, model):
    sample[0].pop(0)
    sample[0].pop(0)
    sample[0].pop(0)
    sample[0].pop(-1)
    sample[0].pop(-1)
    print(sample[0])
    input = torch.FloatTensor(sample[0])
    print(input)
    output = model.forward(input, 1)
    _, predicted = torch.max(output.data, 1)
    return predicted