import os

from model import load_network
from load_data import load_dataset
from game.game import run_game
from src.train.realtime import train_realtime
from src.train.record import train_record


def ask_training():
    while True:
        response = input('Do you want to train this network? (y/n)')

        if response == 'y' or response == 'n':
            break
        print('Invalid input, please type y or n')
    response = True if response == 'y' else False
    return response


def ask_dataset(model):
    print('Which dataset do you want to use?')
    print('1 - Realtime')
    print('2 - Recorded')

    while True:
        response = input()
        response = int(response) if response.isnumeric() else 0

        if 0 < response < 3:
            break
        print('Invalid input, please type 1 or  2')
    if response == 1:
        train_realtime(model)
    else:
        train_record(model)


def get_dataset():
    filepath = "../models/focusdata.csv"
    if not os.path.exists(filepath):
        raise FileNotFoundError('Dataset file does not exist (%s)' % filepath)
    dataset = load_dataset(filepath)
    return dataset


def main():
    model = load_network()
    training = ask_training()
    if training:
        ask_dataset(model)
    dataset = get_dataset()
    run_game(model, dataset)


if __name__ == '__main__':
    main()
