import pygame

pygame.init()


class Button:
    def __init__(self, image, width, height):
        self.image = image
        self.reactImage = self.image.get_rect()
        self.reactImage.topleft = (width, height)
        self.pressed = False
        self.enabled = True

    def draw(self, surface):
        surface.blit(self.image, (self.reactImage.x, self.reactImage.y))

    def check_click(self):
        pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if self.reactImage.collidepoint(pos) and left_click and self.enabled:
            self.pressed = True
        else:
            if self.pressed:
                self.pressed = False
                return True

    def setEnabled(self, boolean):
        self.enabled = boolean
