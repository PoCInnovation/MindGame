from model import load_model
from load_data import load_dataset
from src.game.game import run_game
from os.path import exists


def get_dataset():
    filepath = "../models/focusdata.csv"
    if not exists(filepath):
        raise FileNotFoundError('Model data does not exist (%s)' % filepath)
    dataset = load_dataset(filepath)
    return dataset


def main():
    dataset = get_dataset()
    model = load_model()
    run_game(model, dataset)


if __name__ == '__main__':
    main()
