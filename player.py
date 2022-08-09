import pygame as pg
WHITE = (255, 255, 255)
P_WIDTH, P_HEIGHT = 15, 100

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # draw player's paddle
        self.image = pg.Surface([P_WIDTH, P_HEIGHT])
        pg.draw.rect(self.image, color = WHITE, rect = [0, 0, P_WIDTH, P_HEIGHT])

        # creates a rectangle that can move around in the game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dy):
        HEIGHT = 750

        self.rect.y += dy
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + P_HEIGHT > HEIGHT:
            self.rect.y = HEIGHT - P_HEIGHT
        