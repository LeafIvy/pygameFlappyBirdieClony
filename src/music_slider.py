import pygame as pg


class MusicSlider:
    def __init__(self, x, y, width, color, music):
        self.slider = pg.Rect(x, y, width, 10)
        self.handle = pg.Rect(x, y, 10, 10)
        self.handle.centerx = self.slider.left + (music.get_volume()) * self.slider.width
        self.color = color

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.slider)
        pg.draw.rect(screen, 'black', self.slider, 3)
        pg.draw.circle(screen, self.color, self.handle.center, self.handle.width)
        pg.draw.circle(screen, 'black', self.handle.center, self.handle.width, 3)

    def user_input(self):
        left_click = pg.mouse.get_pressed()[0]
        mouse_pos = pg.mouse.get_pos()
        if left_click and (self.slider.collidepoint(mouse_pos) or self.handle.collidepoint(mouse_pos)):
            self.handle.centerx = mouse_pos[0]

    def update(self):
        self.user_input()

    def get_volume(self):
        return (self.handle.centerx - self.slider.x) / self.slider.width
