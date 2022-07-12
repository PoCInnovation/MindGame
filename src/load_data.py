import pandas as pd
import torch


def load_dataset(path):
    file = pd.read_csv(path)
    df = pd.DataFrame(file)
    df = df.drop(columns=['Unnamed: 33'])

    data = df.to_numpy()
    dataset = list()
    for element in data:
        entry = list()
        entry.append([0] * 32)
        for index, item in enumerate(element):
            if index == 0:
                continue
            entry[0][index - 1] = item
        entry.append(element[0])
        entry[0] = torch.FloatTensor(entry[0])
        dataset.append(entry)
    return dataset
