import os

from model import load_network
from load_data import load_dataset
from game.game import run_game
from src.train.realtime import train_realtime
from src.train.record import train_record


def ask_training():
    print('Do you want to train this network? (y/n)')
    while True:
        response = input()

        if response == 'y' or response == 'n':
            break
        print('Invalid input, please type y or n')
    return True if response == 'y' else False

def ask_testing():
    print('Do you want to test with realtime data or recorded data ?')
    print('1 - Realtime')
    print('2 - Recorded')

    while True:
        response = input()
        response = int(response) if response.isnumeric() else 0

        if 0 < response < 3:
            break
        print('Invalid input, please type 1 or  2')
    if response == 1:
        return True
    else:
        return False

def train_network(network, network_type):
    print('Which dataset do you want to use?')
    print('1 - Realtime')
    print('2 - Record')

    while True:
        response = input()
        response = int(response) if response.isnumeric() else 0

        if 0 < response < 3:
            break
        print('Invalid input, please type 1 or  2')
    if response == 1:
        train_realtime(network, network_type)
    else:
        train_record(network, network_type)


def get_dataset():
    filepath = "../models/focusdata.csv"
    if not os.path.exists(filepath):
        raise FileNotFoundError('Dataset file does not exist (%s)' % filepath)
    dataset = load_dataset(filepath)
    return dataset


def main():
    network, network_type = load_network()
    if ask_training():
        train_network(network, network_type)
        print('Training finished, network can now be used!')
    dataset = get_dataset()
    run_game(network, dataset, ask_testing())


if __name__ == '__main__':
    main()
