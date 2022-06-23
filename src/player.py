import pygame

# define params
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, envsize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../assets/car.png")
        self.image = pygame.transform.scale(self.image, (64, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (envsize[0] / 2, envsize[1] - 80)
    def move(self, label):
        if label == 0:
            self.rect.y -= 1
        if label == 1:
            self.rect.y += 1