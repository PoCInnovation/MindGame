import os
import src.train.runner as runner
import src.load_data as loader
import src.receive_data as recorder


def train_realtime(network, network_type):
    path = recorder.record_eeg()
    if not os.path.exists(path):
        raise FileNotFoundError('Dataset file does not exist (%s)' % path)
    dataset = loader.load_dataset(path)
    network, train_accuracies, test_accuracies = runner.train_network(network, network_type, dataset)
    return network, train_accuracies, test_accuracies
