import pygame as pg
import settings as s

from random import randint
from sys import exit
from player import Player
from pillar import *


pg.init()

screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT))
pg.display.set_caption("Flappy Birdie Copy")

clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
player.add(Player())

pillars = pg.sprite.Group()
headcount = 0
PILLAR = pg.USEREVENT + 1
pg.time.set_timer(PILLAR, 750)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == PILLAR:
            if headcount < 5:
                pillar = PillarHead()
                division = randint(1, ((s.SCREEN_HEIGHT//2)//pillar.rect.height)+1)
                pillar.rect.x = s.SCREEN_WIDTH
                pillar.rect.bottom = division * pillar.rect.height
                pillars.add(pillar)
                headcount += 1
                column = Pillar(pillar)
                while division > 1:
                    pillars.add(column)
                    column = Pillar(column)
                    division -= 1

    screen.fill(s.BG_COLOR)
    player.update()
    player.draw(screen)

    for pillar in pillars:
        pillar.rect.x -= 5
        if pillar.rect.right < 0:
            pillars.remove(pillar)
            headcount -= 1
        elif -pillar.rect.width <= pillar.rect.y <= s.SCREEN_WIDTH:
            screen.blit(pillar.image, pillar.rect)

    pg.display.update()
    clock.tick(s.FPS)
