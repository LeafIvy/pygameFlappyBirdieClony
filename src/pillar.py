import pygame as pg
import settings as s


class PillarHead(pg.sprite.Sprite):
    def __init__(self, straight):
        super().__init__()
        self.passed = False
        image = self.image = pg.transform.scale_by(pg.image.load('graphics/pillar/pillar_head.png').convert_alpha(), 3)
        if straight:
            self.image = image
            self.straight = True
        else:
            self.image = pg.transform.flip(image, False, True)
            self.straight = False
        self.rect = self.image.get_rect()


class Pillar(pg.sprite.Sprite):
    def __init__(self, head, straight):
        super().__init__()
        image = pg.transform.scale_by(pg.image.load('graphics/pillar/pillar.png').convert_alpha(), 3)
        if straight:
            self.image = image
            self.rect = self.image.get_rect(x=head.rect.x, bottom=head.rect.top)
        else:
            self.image = pg.transform.flip(image, False, True)
            self.rect = self.image.get_rect(x=head.rect.x, top=head.rect.bottom)
        
        
