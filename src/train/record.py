import os
import src.train.runner as runner
import src.load_data as loader


def train_record(network):
    input('Put training file into \'models/training.csv\' and press any key to continue...')
    path = '../models/training.csv'
    if not os.path.exists(path):
        raise FileNotFoundError('Dataset file does not exist (%s)' % path)
    dataset = loader.load_dataset(path)
    network, train_accuracies, test_accuracies = runner.train_network(network, dataset)
    return network, train_accuracies, test_accuracies
