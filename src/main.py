import pygame as pg
import settings as s

from sys import exit
from player import Player


pg.init()

screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT))
pg.display.set_caption("Flappy Birdie Copy")

clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
player.add(Player())

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill(s.BG_COLOR)
    player.update()
    player.draw(screen)

    pg.display.update()
    clock.tick(s.FPS)
