from piece import *

class Ruler(object):
    def __init__(self, board):
        self.board = board

    def letInCheck(self, square1, square2):

        x1, y1 = square1
        x2, y2 = square2

        color = self.board[x1][y1].color
        
        case = self.board.case(square1, square2)

        case.next()
        code = self.isCheck(color) 
        case.next()
        
        return code

    def isCheck(self, color):
        king = self.board.findPiece('king', color).next()

        for ind in self.board.squareAttack(king.coord):
            if ind.color != color:
                return True

        return False


    def isCheckMate(self, color):
        if not self.isCheck(color):
            return False
        
        return self.isEnclosed(color)

    def isEnclosed(self, color):
        for indi in self.board.matter(color):
            for indj in indi.pieceReach():
                case = self.board.case(indi.coord, indj)
                case.next()
                code = self.isCheck(color)
                case.next()
                
                if not code:
                    return False
        
        return True


    def isCompliant(self, square1, square2):
        if square1 == square2:
            return False

        x1, y1 = square1
        x2, y2 = square2

        item = self.board[x1][y1]

        if not item: 
            return False
       
        color = item.color

        if color != self.board.player:
            return INVALID

        item = self.board[x2][y2]

        if isinstance(item, King):
            return False

        return True


    def letCheckMate(self, square1, square2):
        case = self.board.case(square1, square2)
        x1, y1 = square1

        color = self.board[x1][y1].oppositeColor()

        case.next()
        try:
            code = self.isCheckMate(color)
        except:
            print self.board[x1][y1]
            print square1, square2
        case.next()

        return code

    def letDraw(self, square1, square2):
        """ Checks for stalemate. """
        x1, y1 = square1

        color = self.board[x1][y1].oppositeColor()

        step = self.board.case(square1, square2)

        step.next()

        code = self.isEnclosed(color)

        step.next()

        return code


    def eval(self, square1, square2):
        x1, y1 = square1
        x2, y2 = square2


        if not self.isCompliant(square1, square2):
            return INVALID

        if self.letInCheck(square1, square2):
            return INVALID

        if self.letCheckMate(square1, square2):
            return CHECK_MATE

        if self.letDraw(square1, square2):
            print 'draw'
            return DRAW

        return self.board[x1][y1].isValidMove(square2)


