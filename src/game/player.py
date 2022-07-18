import pygame

# define params
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../../assets/car.png")
        self.image = pygame.transform.scale(self.image, (64, 80))
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x = 800

        self.input = [0.0, 0.0, 0.0, 0.0]

    def move(self, label):
        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

        ##### Indirect movement
        self.input[label] += 0.1
        for i in range(len(self.input)):
            if i != label:
                self.input[label] -= 0.2
            if self.input[label] < 0:
                self.input[label] = 0
            if self.input[label] > 3:
                self.input[label] = 3
        if self.input[UP] >= 1:
            self.rect.y -= 1
        if self.input[DOWN] >= 1:
            self.rect.y += 1
        if self.input[LEFT] >= 1:
            self.rect.x -= 1
        if self.input[RIGHT] >= 1:
            self.rect.x += 1

        ##### Direct movement
        # if label == UP:
        #     self.rect.y -= 1
        # if label == DOWN:
        #     self.rect.y += 1
        # if label == LEFT:
        #     self.rect.x -= 1
        # if label == RIGHT:
        #     self.rect.x += 1
    def reset(self):
        self.rect.y = 400
        self.rect.x = 800