import pygame
from .constants import white, black, square_side, grey, crown

class Piece:
    padding = 18
    outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        self.x = square_side * self.col + square_side // 2
        self.y = square_side * self.row + square_side // 2

    def King(self):
        self.king = True
    
    def draw_piece(self, win):
        radius = square_side // 2 - self.padding
        pygame.draw.circle(win, grey, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(crown, (self.x - crown.get_width() // 2, self.y - crown.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.position()

    def __repr__(self):
        return str(self.color)