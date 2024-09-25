import pygame as pg
import settings as s

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale2x(pg.image.load("graphics\\bird\\bird_stand.png").convert_alpha())
        self.image_clean = self.image.copy()
        
        self.rect = self.image.get_rect()
        self.reset()

        self.hitbox = pg.Rect(0, 0, 25, 25)
        self.hitbox.center = self.rect.center
        
        self.degrees = 0
        self.images = {}

    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.gravity >= -5 and self.hitbox.top >= 0:
            self.gravity = -6

    def animate(self):
        if self.gravity < 0:
            self.degrees = 45
        elif self.gravity > 0 and self.degrees > -45:
            self.degrees -= 5

        if self.degrees not in self.images:
            self.images[self.degrees] = pg.transform.rotate(self.image_clean, self.degrees)
    
        self.image = self.images[self.degrees]
        self.rect = self.image.get_rect(center=self.rect.center)
        self.hitbox.center = self.rect.center

    def update(self):
        self.gravity += 0.75
        self.player_input()
        self.rect.y += self.gravity
        self.animate()

    def reset(self):
        self.rect.centery = s.SCREEN_HEIGHT//4
        self.rect.left = self.rect.width * 1.5
        self.gravity = 0
