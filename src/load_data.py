import pandas as pd
import torch


def load_dataset(path):
    """Load dataset from filepath passed in parameter
    Dataset will be pre-proceed removing unused columns

    :param path: filepath to dataset
    :return: Pre-processed dataset
    :rtype: list
    """

    file = pd.read_csv(path)
    df = pd.DataFrame(file)
    df = df.drop(columns=['Unnamed: 33'])

    data = df.to_numpy()
    dataset = list()
    for element in data:
        entry = [0] * 32
        for index, item in enumerate(element):
            if index == 0:
                continue
            entry[index - 1] = item
        entry = torch.FloatTensor(entry)
        dataset.append((entry, int(element[0])))
    return dataset
