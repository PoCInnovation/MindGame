import pygame

# define params
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../assets/car.png")
        self.image = pygame.transform.scale(self.image, (64, 80))
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x = 800
    def move(self, label):
        if label == 0:
            self.rect.y -= 1
        if label == 1:
            self.rect.y += 1
        if label == 2:
            self.rect.x -= 1
        if label == 3:
            self.rect.x += 1
    def reset(self):
        self.rect.y = 400
        self.rect.x = 800