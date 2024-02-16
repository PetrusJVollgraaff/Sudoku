import pygame
from board import Board
from board2 import Board2
from Settings import *
pygame.font.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_text(text, color, top, left, font ):
    label = font.render(text, 1, color)
    win.blit(label, (top - (label.get_width()/2), left - (label.get_height()/2)) )


def main():
    bo = Board()
    bo.build_grid()

    #bo2 = Board2()
    #bo2.build_grid()

    run = True

    row = 0
    col = 0
    selected = False

    while run:
        bo.draw_board(win)
        #bo2.draw_board(win)

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
                    bo.set_Value(row, col, int(event.unicode))

        pygame.display.update()


def StartMenu():
    run = True
    font = pygame.font.SysFont('comicsans', 20, bold=True)
    top = WIDTH / 2
    left = HEIGHT / 2

    while run:
        win.fill((0, 0, 0))
        draw_text("Press Any Key To Play", (255, 255, 255), top, left, font)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                main()

    pygame.display.quit()


pygame.display.set_caption("Sudoku Game")
StartMenu()