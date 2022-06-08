import pygame

# define params
WIDTH = 360
HEIGHT = 480
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../assets/car.png")
        self.image = pygame.transform.scale(self.image, (64, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 80)
        self.angle = 0
    def update(self):
        if (self.rect.y < 0):
            self.rect.y = HEIGHT
        if (self.rect.y > HEIGHT):
            self.rect.y = 0
    def move(self, label):
        if label == 0:
            self.rect.y -= 3
        if label == 1:
            self.rect.y += 1