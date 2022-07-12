import random
import torch
import pandas as pd
import numpy as np


def get_mean_electrode(slice, electrode):
    value = 0
    for i in range(slice.shape[0]):
        value += slice[i][electrode]
    return value / slice.shape[0]


def get_mean_values(dataset):
    mean_values = [0] * dataset.shape[0]
    for i in range(dataset.shape[0]):
        mean_values[i] = dataset[i].mean()
    return mean_values


def rescale_dataset(dataset, scale):
    scaled_set = torch.zeros([(int)(dataset.shape[0] / scale), dataset.shape[1]])
    for i in range(scaled_set.shape[0]):
        slice_of_ten = dataset[(i * scale):(i * scale + scale)]
        for j in range(scaled_set.shape[1]):
            scaled_set[i][j] = get_mean_electrode(slice_of_ten, j)
    return scaled_set


def convert_dataset(path):
    file = pd.read_csv(path, skiprows=1,
                    usecols=['EEG.Cz', 'EEG.Fz', 'EEG.Fp1', 'EEG.F7',
                            'EEG.F3', 'EEG.FC1', 'EEG.C3', 'EEG.FC5',
                            'EEG.FT9', 'EEG.T7', 'EEG.CP5', 'EEG.CP1',
                            'EEG.P3', 'EEG.P7', 'EEG.PO9', 'EEG.O1',
                            'EEG.Pz', 'EEG.Oz', 'EEG.O2', 'EEG.PO10',
                            'EEG.P8', 'EEG.P4', 'EEG.CP2', 'EEG.CP6',
                            'EEG.T8', 'EEG.FT10', 'EEG.FC6', 'EEG.C4',
                            'EEG.FC2', 'EEG.F4', 'EEG.F8', 'EEG.Fp2'])
    df = pd.DataFrame(file)
    vanilla_data = df.to_numpy()
    normalized_data = (vanilla_data - np.min(vanilla_data)) / (np.max(vanilla_data) - np.min(vanilla_data))
    standardized_data = normalized_data - normalized_data.mean()
    large_data = torch.Tensor(standardized_data)

    return rescale_dataset(large_data, 10)


def split_data(dataset):
    random.shuffle(dataset)
    train_size = (int)(len(dataset) * 0.8)
    test_size = len(dataset) - train_size
    train_set = dataset[0:train_size]
    test_set = dataset[train_size:train_size+test_size]
    return train_set, test_set
