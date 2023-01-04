import pygame
from Config.config import *
import numpy as nump
from Abstract import *


class GameController(GameAbstract):
    def __init__(self):
        self.__size = 10

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def update(self, window, cells):
        up_cells = nump.zeros((cells.shape[0], cells.shape[1]))
        for row, col in nump.ndindex(cells.shape):
            life = nump.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]

            if (cells[row, col] == 1 and 2 <= life <= 3) or (cells[row, col] == 0 and life == 3):
                up_cells[row, col] = 1
                color = COLOR_LIFE
            color = color if cells[row, col] == 1 else COLOR_DIE
            pygame.draw.rect(window, color, (col * self.size, row * self.size, self.size - 1, self.size - 1))
        return up_cells

    def playing_field(self, window, cells):
        for row, col in nump.ndindex(cells.shape):
            color = SCREEN_COLOR if cells[row, col] == 0 else COLOR_LIFE
            pygame.draw.rect(window, color, (col * self.size, row * self.size, self.size - 1, self.size - 1))
