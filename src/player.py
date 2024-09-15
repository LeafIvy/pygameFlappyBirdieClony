import pygame as pg
import settings as s

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale(pg.image.load("src\\graphics\\bird\\bird_stand.png").convert_alpha(), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.centery = s.SCREEN_HEIGHT//2
        self.rect.left = self.rect.width * 1.5

