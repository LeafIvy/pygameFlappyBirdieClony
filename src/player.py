import pygame as pg
import settings as s

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale(pg.image.load("src\\graphics\\bird\\bird_stand.png").convert_alpha(), (64, 64))
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.centery = s.SCREEN_HEIGHT//2
        self.rect.left = self.rect.width * 1.5

        self.gravity = 0
        self.degrees = 0

    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.gravity >= -5:
            self.gravity = -10

    def animate(self):
        if self.gravity < 0:
            self.degrees = 45
            self.image = pg.transform.rotate(self.image_clean, 45)
        if self.gravity > 0:
            if self.degrees > -45: self.degrees -= 5
            self.image = pg.transform.rotate(self.image_clean, self.degrees)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.gravity += 0.75
        self.player_input()
        self.rect.y += self.gravity
        self.animate()

