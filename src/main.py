import pygame as pg
from sys import exit

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Flappy Birdie Copy")

clock = pg.time.Clock()
FPS = 60

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()
    clock.tick(FPS)
