import pygame as pg
import settings as s

from random import randint
from sys import exit
from player import Player
from pillar import *
from button import Button

pg.init()

screen = pg.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pg.display.set_caption("Flappy Birdie Copy")

game_active = False

clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
player.add(Player())


def play_clicked():
    global game_active
    game_active = True
    player.sprite.reset()

    
play_button = Button(0, 0, 'Play', None, 50, 'blue', 'green', play_clicked, 25)
play_button.rect.center = screen_rect.center

pillars = pg.sprite.Group()
headcount = 0
PILLAR = pg.USEREVENT + 1
pg.time.set_timer(PILLAR, 750)


def create_pillars():
    pillarS = PillarHead(True)
    pillarF = PillarHead(False)
    
    division = randint(1, (s.SCREEN_HEIGHT//pillarS.rect.height) - 2)
    pillarS.rect.x = pillarF.rect.x = s.SCREEN_WIDTH
    
    pillarS.rect.bottom = division * pillarS.rect.height
    pillarF.rect.top = (division + 2) * pillarF.rect.height
    
    pillars.add(pillarS)
    pillars.add(pillarF)
    
    columnS = Pillar(pillarS, True)
    columnF = Pillar(pillarF, False)
    
    while columnS.rect.top > -columnS.rect.height:
        pillars.add(columnS)
        columnS = Pillar(columnS, True)

    while columnF.rect.bottom < s.SCREEN_HEIGHT + columnF.rect.height:
        pillars.add(columnF)
        columnF = Pillar(columnF, False)

def pillar_update():
    global headcount
    for pillar in pillars:
        pillar.rect.x -= 5
        if pillar.rect.right < 0:
            pillars.remove(pillar)
            headcount -= 1


def check_collision():
    for pillar in pillars:
        if player.sprite.hitbox.colliderect(pillar.rect):
            return False
    if player.sprite.hitbox.bottom >= s.SCREEN_HEIGHT: return False
    return True
        
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if game_active:
            if event.type == PILLAR:
                if headcount < 5:
                    create_pillars()
                    headcount += 1

    if game_active:
        screen.fill(s.BG_COLOR)
        player.update()
        pillar_update()
        game_active = check_collision()
        if screen_rect.colliderect(player.sprite.rect): player.draw(screen)
        pillars.draw(screen)
        pg.draw.rect(screen, 'black', player.sprite.hitbox, 1)
    else:
        pillars.empty()
        headcount = 0
        play_button.draw(screen)
        play_button.clicked()
    
    pg.display.update()
    clock.tick(s.FPS)
