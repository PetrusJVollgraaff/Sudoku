import random
from Settings import *
from block import *

class Board:

    def __init__(self):
        self.input_boxes = [[Block(j, i) for j in range(9)] for i in range(9)]
        self._9block = [[0 for _ in range(9)] for _ in range(9)]

    def build_grid(self):

        test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(9):
            index = random.randint(0, len(test_array) - 1)
            num = test_array[index]
            self.input_boxes[0][i].set_Num(num)
            test_array.remove(num)

        self.resolve_grid()
        self.create_empty()

    def resolve_grid(self):
        for i, row in enumerate(self.input_boxes):
            for j, block in enumerate(row):
                if self.input_boxes[i][j].get_Num() == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(i, j, num):
                            self.input_boxes[i][j].set_Num(num)
                            if self.resolve_grid():
                                return True
                            self.input_boxes[i][j].set_Num(0)
                    return False
        return True

    def is_valid_move(self, row, col, num):
        # Check if the number is not in the same row or column
        if self.is_in_row(row, num) or self.is_in_col(col, num):
            return False

        # Check if the number is not in the same 3x3 subgrid
        if self.is_3x3(row, col, num):
            return False

        return True

    def is_in_row(self, row, num):
        for i in range(9):
            if self.input_boxes[row][i].get_Num() == num:
                return True

        return False

    def is_in_col(self, col, num):
        for i in range(9):
            if self.input_boxes[i][col].get_Num() == num:
                return True

        return False

    def is_3x3(self, row, col, num):
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.input_boxes[start_row + i][start_col + j].get_Num() == num:
                    return True

        return False

    def create_empty(self):
         #Remove numbers to create the puzzle
         for _ in range(20):  # Adjust the number of cells to remove as needed
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.input_boxes[row][col].get_Num() == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)

            self.input_boxes[row][col].set_Num( 0 )
            self.input_boxes[row][col].set_edit(True)

    def draw_board(self, win):
        win.fill(WHITE)

        for i in range(9):
            for j in range(9):
                backcolor = GRAY2
                textcolor = WHITE

                if self.input_boxes[j][i].isSelected:
                    backcolor = RED
                    textcolor = BLACK
                elif not self.input_boxes[j][i].isValid:
                    backcolor = YELLOW
                    textcolor = BLACK
                elif self.input_boxes[j][i].isEditable:
                    backcolor = GRAY
                    textcolor = BLACK


                pygame.draw.rect(win, backcolor, self.input_boxes[j][i].get_Rect())
                num = self.input_boxes[j][i].get_Num()

                if num != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(num), True, textcolor)
                    win.blit(text, (i * 50 + 20, j * 50 + 15))

        # Draw grid lines
        for i in range(10):
            color = WHITE

            if i == 3 or i == 6:
                color = BLACK

            pygame.draw.line(win, color, (0, i * 50), (450, i * 50), 2)
            pygame.draw.line(win, color, (i * 50, 0), (i * 50, 450), 2)

    def isEditable(self, row, col):
        return self.input_boxes[row][col].get_Editable()

    def set_Selected(self, row, col):
        self.reset_selected()
        self.input_boxes[row][col].set_Selected(True)

    def reset_selected(self):
        for row in self.input_boxes:
            for block in row:
                block.set_Selected(False)

    def set_Value(self, row, col, value):
        self.input_boxes[row][col].set_Num(value)

        isvalid = self.is_valid_move(row, col, value)

        self.input_boxes[row][col].set_valid(isvalid)
