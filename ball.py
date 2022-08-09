import pygame
from random import randint
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # ball with radius 10, inside a surface of size 10 x 10
        self.image = pygame.Surface([10, 10])

        # draw the ball
        pygame.draw.rect(self.image, color = WHITE, rect = [0, 0, 10, 10])

        self.v_x = randint(4,7)
        self.v_y = randint(-10,10)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def move(self):
        self.rect.x += self.v_x
        self.rect.y += self.v_y

    def bounce(self):
        self.v_x = - self.v_x
        self.v_y = randint(-10,10)
