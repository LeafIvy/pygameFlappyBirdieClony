import pygame as pg

from sys import exit
import settings as s

pg.init()

screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT))
pg.display.set_caption("Flappy Birdie Copy")

clock = pg.time.Clock()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill(s.BG_COLOR)

    pg.display.update()
    clock.tick(s.FPS)
