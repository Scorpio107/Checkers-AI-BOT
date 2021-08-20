import pygame
from .constants import white, black, square_side, grey, crown, blue
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = black
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.select_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.select_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.select_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move_piece(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, blue, (col * square_side + square_side // 2, row * square_side + square_side // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == white:
            self.turn = black
        else:
            self.turn = white

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()