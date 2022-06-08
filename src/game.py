import pygame
import torch

from load_data import load_dataset
from neuralnetwork import NeuralNetwork
from player import Player
from prediction import get_prediction

dataset = load_dataset("../models/focusdata.csv")
DATA_LENGTH = len(dataset)

model = NeuralNetwork()
model.load_state_dict(torch.load("../models/network.pt"))
model.eval()

# define params
WIDTH = 360
HEIGHT = 480
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MindGame")

class Game():
    def __init__(self):
        self.running = True
        self.font = pygame.freetype.Font("../assets/ComicSansMS3.ttf", 24)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.data_index = 0

        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def draw(self):
        # Draw / render
        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        self.font.render_to(self.screen, (10, 10), str(self.data_index), (0, 0, 0))
        pygame.display.flip()

    def update(self):
        self.all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        label = get_prediction(self.data_index, dataset, model)
        self.player.move(label)
        if (self.data_index < DATA_LENGTH - 1):
            self.data_index += 1
        else:
            self.data_index = 0

    def loop(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.draw()
            self.update()

game = Game()
game.loop()

pygame.quit()