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
pg.display.set_icon(pg.image.load('flappy_bird.ico').convert_alpha())

bgmusic = pg.mixer.Sound('audio/bgm.mp3')
bgmusic.play(-1)
scored = pg.mixer.Sound('audio/score.wav')
lost = pg.mixer.Sound('audio/lose.wav')

game_active = False
first_out = False

clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
player.add(Player())


def settings_screen():
    pass


settings_button = Button(0, s.SCREEN_HEIGHT - 64, onClick=settings_screen)
settings_button.make_msg(12, 1, pg.image.load('graphics/settings/settings.png').convert_alpha())


def play_clicked():
    global game_active, score
    game_active = True
    score = 0
    pillars.empty()
    player.sprite.reset()


play_button = Button(0, 0, 'Play', None, 50, 'blue', 'green', 25, True, onClick=play_clicked)
play_button.rect.center = screen_rect.center

score = 0
score_surf = Button(0, 0, f'SCORE: {score}', None, 50, 'gold', 'nocolor', 10, False, None)

pillars = pg.sprite.Group()
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
    global score
    for pillar in pillars:
        pillar.rect.x -= s.SPEED
        if type(pillar) == PillarHead and pillar.straight:
            if game_active and (pillar.rect.right <= player.sprite.rect.left and not pillar.passed):
                score += 1
                scored.play()
                pillar.passed = True
        if pillar.rect.right < 0:
            pillars.remove(pillar)
    score = int(score)

def check_collision():
    for pillar in pillars:
        if player.sprite.hitbox.colliderect(pillar.rect):
            return False
    if player.sprite.hitbox.bottom >= s.SCREEN_HEIGHT: return False
    return True


highscore = 0
try:
    with open('highscore.txt', 'r') as f:
        highscore = int(f.readline())
except FileNotFoundError:
    with open('highscore.txt', 'w') as f:
        f.write(str(highscore))
highscore_surf = Button(s.SCREEN_WIDTH/2, 0, f'HIGHSCORE: {highscore}', None, 50, 'gold', 'nocolor', 10, False, None)
print(highscore)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == PILLAR:
            create_pillars()

    screen.fill('cyan')
    pillar_update()
    pillars.draw(screen)
    if game_active:
        player.update()
        game_active = check_collision()
        if not game_active:
            lost.play()
            first_out = True
        if screen_rect.colliderect(player.sprite.rect): player.draw(screen)
    else:
        if first_out:
            if screen_rect.colliderect(player.sprite.rect): player.draw(screen)
            player.sprite.rect.x -= s.SPEED
        if score > highscore:
            with open('highscore.txt', 'w') as f:
                f.write(str(score))
                highscore = score
        play_button.draw(screen)
        play_button.clicked()
        highscore_surf.message = f'HIGHSCORE: {highscore}'
        highscore_surf.make_msg(highscore_surf.message, highscore_surf.textColor)
        highscore_surf.draw(screen)

    score_surf.message = f'SCORE: {score}'
    score_surf.make_msg(score_surf.message, score_surf.textColor)
    score_surf.draw(screen)

    settings_button.draw(screen)
    
    pg.display.update()
    clock.tick(s.FPS)
