import random
import pygame
from Settings import *
from block import *

def checkArry(array):
    num = random.randint(1, 9)
    while num in array:
        num = checkArry(array)

    return num

class Board:

    def __init__(self):
        self.answer_board = [[0 for x in range(9)] for _ in range(9)]
        self.board = [[0 for x in range(9)] for _ in range(9)]
        self.input_boxes = [[pygame.Rect(j * 50, i * 50, 50, 50) for j in range(9)] for i in range(9)]

        self.input_boxes1 = [[Block(j, i) for j in range(9)] for i in range(9)]

    def build_grid(self):
        for i, row in enumerate(self.input_boxes1):
            for j, block in enumerate(row):
                rowArr = []
                num = checkArry(rowArr)

                if self.is_valid_move(i, j, num):
                    self.input_boxes1[i][j].set_Num(num)
                    self.input_boxes1[i][j].set_edit(False)
                    rowArr.append(num)

    def is_valid_move(self, row, col, num):
        # Check if 'num' is not present in the current row, column, and the 3x3 subgrid
        return all(
            num != self.input_boxes1[row][i].get_Num() and
            num != self.input_boxes1[i][col].get_Num()
            and num != self.input_boxes1[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3].get_Num()
            for i in range(9)
        )

    def draw_board(self, win):
        win.fill(WHITE)

        for i in range(9):
            for j in range(9):
                backcolor = BLACK
                textcolor = WHITE

                if self.input_boxes1[j][i].isSelected:
                    backcolor = RED
                    textcolor = BLACK
                elif self.input_boxes1[j][i].isEditable:
                    backcolor = GRAY
                    textcolor = BLACK

                pygame.draw.rect(win, backcolor, self.input_boxes1[j][i].get_Rect())
                num = self.input_boxes1[j][i].get_Num()
                if num != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(num), True, textcolor)
                    win.blit(text, (i * 50 + 20, j * 50 + 15))

        # Draw grid lines
        for i in range(10):
            pygame.draw.line(win, WHITE, (0, i * 50), (450, i * 50), 2)
            pygame.draw.line(win, WHITE, (i * 50, 0), (i * 50, 450), 2)

    def isEditable(self, row, col):
        return self.input_boxes1[row][col].get_Editable()

    def set_Selected(self, row, col):
        self.reset_selected()
        self.input_boxes1[row][col].set_Selected(True)

    def reset_selected(self):
        for row in self.input_boxes1:
            for block in row:
                block.set_Selected(False)

    def set_Value(self, win, row, col, value):
        self.input_boxes1[row][col].set_Num(value)