# game.py - This is the pong game that will be controlled with the OpenBCI headset.
import pygame
from player import Player
from ball import Ball
pygame.init()
pygame.font.init()

# Settings
WIDTH, HEIGHT = 1250, 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60 
ICON = pygame.image.load('assets/icon.png')
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(ICON)
pygame.display.set_caption("Pong")
font = pygame.font.Font('assets/basis33.ttf', 64)
clock = pygame.time.Clock()


# Players
P_WIDTH = 15
P_HEIGHT = 100

player1Score = 0
player1 = Player(x = 30, y = HEIGHT//2)

player2Score = 0
player2 = Player(x = WIDTH - 45, y = HEIGHT//2)

# Ball
ball = Ball(WIDTH//2,HEIGHT//2)

all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False

            if event.type == pygame.KEYDOWN:
                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    running = False

        key = pygame.key.get_pressed() 
        if key[pygame.K_UP]:
            player1.move(-5)
        if key[pygame.K_DOWN]:
            player1.move(5)

        all_sprites.update()
        
        # Check if the ball touched any wall
        if ball.rect.x >= WIDTH:
            ball.v_x = -ball.v_x
        if ball.rect.x <= 0:
            ball.v_x = -ball.v_x
        if ball.rect.y > HEIGHT:
            ball.v_y = -ball.v_y
        if ball.rect.y < 0:
            ball.v_y = -ball.v_y 
        
        window.fill(BLACK)
        display_score()
        all_sprites.draw(window)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

def display_score():
    score1 = font.render(str(player1Score), True, WHITE)
    score2 = font.render(str(player2Score), True, WHITE)
    score1Rect = score1.get_rect()
    score2Rect = score2.get_rect()
    score1Rect.center = (WIDTH * 0.4, HEIGHT * 0.1)
    score2Rect.center = (WIDTH * 0.6, HEIGHT * 0.1)
    window.blit(score1, score1Rect)
    window.blit(score2, score2Rect)

if __name__ == "__main__":
    main()