import pygame

class Block:

    def __init__(self, x1, y1, ):
        self.x1 = x1
        self.y1 = y1
        self.rect = pygame.Rect(self.x1 * 50, self.y1 * 50, 50, 50)
        self.num = 0
        self.isSelected = False
        self.isEditable = False

    def set_Num(self, num):
        self.num = num

    def set_edit(self, value):
        self.isEditable = value

    def set_Selected(self,value):
        self.isSelected = value
    def get_Num(self):
        return self.num

    def get_Rect(self):
        return self.rect


    def isSelected(self):
        return self.isSelected


    def get_Editable(self):
        return self.isEditable