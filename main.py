import pygame
from board import Board
from Settings import *
pygame.font.init()

def main(win):
    bo = Board()
    bo.build_grid()
    run = True

    row = 0
    col = 0
    selected = False

    while run:
        bo.draw_board(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = pygame.mouse.get_pos()[1] // 50, pygame.mouse.get_pos()[0] // 50
                if bo.isEditable(row, col):
                    bo.set_Selected(row, col)
                    selected = True

            if event.type == pygame.KEYDOWN:
                if selected and event.unicode.isdigit():
                    bo.set_Value(win, row, col, int(event.unicode))

        pygame.display.update()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")
main(win)