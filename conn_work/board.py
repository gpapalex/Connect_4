import pygame
from .myvars import *
import numpy as np


class Board:
    def __init__(self):
        self.red_dropped = self.yellow_dropped = 0
        self.create_board()

    def create_board(self):
        self.board = np.zeros((ROWS,COLS))

    def draw(self, win):
        for row  in range(COLS):
            for col in range(ROWS):
                pygame.draw.rect(win, rgb_list[4], (row*SQUARE_SIZE, (col+1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.circle(win, rgb_list[0], ((row*SQUARE_SIZE+SQUARE_SIZE//2), ((col+1)*SQUARE_SIZE+SQUARE_SIZE//2)), RADIUS)


                