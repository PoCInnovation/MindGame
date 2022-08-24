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

        self.input = [0.0, 0.0, 0.0, 0.0]

    def move(self, label):
        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        SPEED = 1
        MOVEMENT = 10

        self.input[label] += SPEED

        print(f"UP:\t{self.input[UP]}%")
        print(f"DOWN:\t{self.input[DOWN]}%")
        print(f"LEFT:\t{self.input[LEFT]}%")
        print(f"RIGHT:\t{self.input[RIGHT]}%")

        if self.input[label] >= 100:
            if label == UP:
                self.rect.y -= MOVEMENT
            if label == DOWN:
                self.rect.y += MOVEMENT
            if label == LEFT:
                self.rect.x -= MOVEMENT
            if label == RIGHT:
                self.rect.x += MOVEMENT
            self.input = [0.0, 0.0, 0.0, 0.0]

    def reset(self):
        self.rect.y = 400
        self.rect.x = 800