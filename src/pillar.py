import pygame as pg
import settings as s


class PillarHead(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale_by(pg.image.load('src/graphics/pillar/pillar_head.png').convert_alpha(), 3)
        self.rect = self.image.get_rect()


class Pillar(pg.sprite.Sprite):
    def __init__(self, head):
        super().__init__()

        self.image = pg.transform.scale_by(pg.image.load('src/graphics/pillar/pillar.png').convert_alpha(), 3)
        self.rect = self.image.get_rect(x=head.rect.x, bottom=head.rect.top)
        
