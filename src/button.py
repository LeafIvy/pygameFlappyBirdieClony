import pygame as pg


class Button:
    def __init__(self, x, y, message=None, font=None, size=10, textColor='black', buttonColor='nocolor', padding=0, showpadding=False, onClick=None):
        self.message = message
        self.textColor = textColor
        self.x = x
        self.y = y
        self.font = pg.font.Font(font, size)
        self.make_msg(self.message, self.textColor)
        self.size = self.rect.size
        self.rect.size = (self.rect.width+padding, self.rect.height+padding) 
        self.onClick = onClick
        self.color = buttonColor
        self.showpadding = showpadding

    def make_msg(self, msg, color, image=None):
        if image: self.image = image
        else: self.image = self.font.render(msg, True, color)
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    def draw(self, screen):
        if self.color != 'nocolor': pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.centerx-self.size[0]/2, self.rect.centery-self.size[1]/2))
        if self.showpadding: pg.draw.rect(screen, 'black', self.rect, 5)

    def clicked(self):
        if self.onClick != None:
            mouse_button = pg.mouse.get_pressed()
            mouse_pos = pg.mouse.get_pos()
            if mouse_button[0] and self.rect.collidepoint(mouse_pos): self.onClick()
        
