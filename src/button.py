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
        self.hasimage = False
        self.click = True

    def make_msg(self, msg, color, image=None):
        if image:
            self.hasimage = True
            self.image = image
        else: self.image = self.font.render(msg, True, color)
        self.rect = self.image.get_rect(x=self.x, y=self.y)

    def draw(self, screen):
        if self.color != 'nocolor': pg.draw.rect(screen, self.color, self.rect)
        if self.hasimage: screen.blit(self.image, self.rect)
        else: screen.blit(self.image, (self.rect.centerx-self.size[0]/2, self.rect.centery-self.size[1]/2))
        if self.showpadding: pg.draw.rect(screen, 'black', self.rect, 5)

    def clicked(self):
        mouse_pos = pg.mouse.get_pos()
        left_click = pg.mouse.get_pressed()[0]
        if self.click and (left_click and self.rect.collidepoint(mouse_pos)):
            self.onClick()
            self.click = False
        if not left_click: self.click = True
        
        
