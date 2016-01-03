from mate.ruler import *
from mate.board import *
from mate.piece import *
import time


class Game(object):
    def __init__(self, **args):
        self.board = Board()
        self.reset()

    def move(self, code, square1, square2, promote=Pawn):
        code = self.board.move(code, square1, square2, promote)

        return code


    def reset(self):
        self.board.reset()

        self.initialTime = 0


        Rook(self.board, BLACK, (0, 0))
        Knight(self.board, BLACK, (0, 1))
        Bishop(self.board, BLACK, (0, 2))
        Queen(self.board, BLACK, (0, 3))
        King(self.board, BLACK, (0, 4))
        Bishop(self.board, BLACK, (0, 5))
        Knight(self.board, BLACK, (0, 6))
        Rook(self.board, BLACK, (0, 7))
        Pawn(self.board, BLACK, (1, 0))
        Pawn(self.board, BLACK, (1, 1))
        Pawn(self.board, BLACK, (1, 2))
        Pawn(self.board, BLACK, (1, 3))
        Pawn(self.board, BLACK, (1, 4))
        Pawn(self.board, BLACK, (1, 5))
        Pawn(self.board, BLACK, (1, 6))
        Pawn(self.board, BLACK, (1, 7))

        Rook(self.board, WHITE, (7, 0))
        Knight(self.board, WHITE, (7, 1))
        Bishop(self.board, WHITE, (7, 2))
        Queen(self.board, WHITE, (7, 3))
        King(self.board, WHITE, (7, 4))
        Bishop(self.board, WHITE, (7, 5))
        Knight(self.board, WHITE, (7, 6))
        Rook(self.board, WHITE, (7, 7))
        Pawn(self.board, WHITE, (6, 0))
        Pawn(self.board, WHITE, (6, 1))
        Pawn(self.board, WHITE, (6, 2))
        Pawn(self.board, WHITE, (6, 3))
        Pawn(self.board, WHITE, (6, 4))
        Pawn(self.board, WHITE, (6, 5))
        Pawn(self.board, WHITE, (6, 6))
        Pawn(self.board, WHITE, (6, 7))


