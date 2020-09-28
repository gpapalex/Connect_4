import pygame
from .myvars import *
from conn_work.board import Board

class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.board = Board()
        self.turn = rgb_list[6]
        
    def is_valid_move(self, board, col):
        return board[ROWS - 1][col] == 0

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def get_next_open_row(self, board, col):
        for i in range(ROWS):
            if board[i][col] == 0:
                return i
    
    def drop_piece(self, row, col, piece):
        board[row][col] = piece
        self.change_turn()

    def change_turn(self):
        if self.turn == rgb_list[6]:
            self.turn = rgb_list[2]
        else:
            self.turn = rgb_list[6]
