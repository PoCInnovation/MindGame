import torch
import pygame

from src.game.player import Player
from src.prediction import get_prediction
from pylsl import StreamInlet, resolve_stream

# define params
WIDTH = 1600
HEIGHT = 900
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def run_game(model, dataset, realtime):
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("MindGame")

    game = Game(model, dataset, realtime)
    game.loop()

    pygame.quit()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, src, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(src)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()


class Game:
    def __init__(self, model, dataset, realtime):
        if realtime:
            print("looking for an EEG stream...")
            self.streams = resolve_stream('type', 'EEG')
            self.inlet = StreamInlet(self.streams[0])

        self.running = True
        self.font = pygame.freetype.Font("../assets/ComicSansMS3.ttf", 24)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.data_index = 0

        self.realtime = realtime
        self.model = model
        self.dataset = dataset
        self.data_length = len(dataset)
        self.player = Player()
        self.background = Sprite("../assets/road.png", (WIDTH, HEIGHT))

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.background)
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
        if self.realtime:
            # stream realtime data
            sample = self.inlet.pull_sample()
            sample = torch.FloatTensor(sample[0])[3:-2]
        else:
            # work with recorded data
            sample = self.dataset[self.data_index]
            sample = torch.FloatTensor(sample[0])
        label = get_prediction(sample, self.model)
        self.player.move(label)
        if self.data_index < self.data_length - 1:
            self.data_index += 1
        else:
            self.data_index = 0

    def loop(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.draw()
            self.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.player.reset()
