import pygame as pg


class Button:
    def __init__(self, x, y, message, font, size, textColor, buttonColor, onClick, padding):
        self.font = pg.font.Font(font, size)
        self.image = self.font.render(message, True, textColor)
        self.rect = self.image.get_rect(x=x, y=y)
        self.size = self.rect.size
        self.rect.size = (self.rect.width+padding, self.rect.height+padding) 
        self.onClick = onClick
        self.color = buttonColor

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.centerx-self.size[0]/2, self.rect.centery-self.size[1]/2))
        pg.draw.rect(screen, 'black', self.rect, 5)

    def clicked(self):
        mouse_button = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        if mouse_button[0] and self.rect.collidepoint(mouse_pos): self.onClick()
        
