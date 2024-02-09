import pygame
from board import Board
from Settings import *
pygame.font.init()

def draw_text(win, text, color, top, left, font ):
    label = font.render(text, 1, color)

    win.blit(label, (top - (label.get_width()/2), left - (label.get_height()/2)) )
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

def StartMenu(win):
    run = True
    font = pygame.font.SysFont('comicsans', 20, bold=True)
    top = WIDTH / 2
    left = HEIGHT / 2

    while run:
        win.fill((0, 0, 0))
        draw_text(win, "Press Any Key To Play", (255, 255, 255), top, left, font)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")
StartMenu(win)