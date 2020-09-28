import pygame
from conn_work.myvars import *
from conn_work.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AI CONNECT-4 2020 PYGAME')


def get_mouse_row_col_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



def main():
    flag = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    

    while flag:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_row_col_pos(pos)
        
        game.update()
                

    pygame.quit()  


main()