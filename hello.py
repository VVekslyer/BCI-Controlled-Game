from pygame import *

init()
font.init()

WIDTH, HEIGHT = 1250, 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60 
ICON = image.load('assets/icon.png')
window = display.set_mode((WIDTH, HEIGHT))
display.set_icon(ICON)
display.set_caption("Pong")
font = font.Font('assets/basis33.ttf', 64)
clock = time.Clock()