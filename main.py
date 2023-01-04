import sys
import time
import pygame
from Buttons import *
from Controller import *
import numpy as n
from Config.config import *

pygame.init()


def scaleImage(image, scale=SCALE):
    return pygame.transform.scale(image, scale)


def getImage(pathIcon):
    return scaleImage(pygame.image.load(f'img/{pathIcon}').convert_alpha())


def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    cells = n.zeros(CELLS_SETTING)

    screen.fill(SCREEN_COLOR)
    Game = GameController()
    pygame.display.set_caption(TITLE_WINDOW)

    BUTTON_START = Button(getImage(ICON_START), ((WINDOW_WIDTH / 2) - 40), ICON_TOP)
    BUTTON_REFRESH = Button(getImage(ICON_REFRESH), ((WINDOW_WIDTH / 2) - 100), ICON_TOP)
    BUTTON_NEXT = Button(getImage(ICON_NEXT), ((WINDOW_WIDTH / 2) + 20), ICON_TOP)

    BUTTON_START.draw(screen)
    BUTTON_NEXT.draw(screen)
    BUTTON_REFRESH.draw(screen)
    pygame.display.flip()
    pygame.display.update()

    running = False
    while True:

        screen.fill(SCREEN_GRID)
        Game.playing_field(screen, cells)

        if BUTTON_START.check_click():
            running = not running
        if BUTTON_NEXT.check_click() and not running:
            cells = Game.nextSteps(screen, cells)
        if BUTTON_REFRESH.check_click() and not running:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0] and not running:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                Game.playing_field(screen, cells)

        if running:
            cells = Game.update(screen, cells)
        else:
            Game.playing_field(screen, cells)

        BUTTON_START.draw(screen)
        BUTTON_NEXT.draw(screen)
        BUTTON_REFRESH.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
