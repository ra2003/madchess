from geo import *

INVALID      = 0
CHECK        = 1
CHECK_MATE   = 2
PROMOTION      = 3
TAKE         = 4
DRAW         = 5
VALID        = 6
ENPASANT     = 7
KING_CASTLE  = 8
QUEEN_CASTLE = 9
WHITE_WIN    = 10
BLACK_WIN    = 11
WHITE        = 12
BLACK        = 13

class Piece(object):
    def __init__(self, board,  color, coord):
        self.board = board
        self.color = color
        self.coord = coord
        self.count = 0 

        x, y = coord
        self.board[x][y] = self

    def pieceReach(self):
        pass

    def __str__(self):
        pass

    def isOppositeColor(self, square):
        x, y = square
        other = self.board[x][y]
        
        return other.color != self.color


    def isValidSquare(self, square):
        x, y = square

        item = self.board[x][y]

        if item:
            if not self.isOppositeColor(square):
                return False

        return True

    def oppositeColor(self):
        if self.color == WHITE:
            return BLACK
        else:
            return WHITE

    def oppositeSide(self, square):
        pass

    def attackReach(self):
        pass

    def isValidMove(self, square):
        return INVALID
        pass

class Bishop(Piece):
    def __init__(self, board, color, coord):
        Piece.__init__(self, board, color, coord)
        self.type = 'bishop'

    def pieceReach(self):
        for ind in isOnRight(self.coord):
            if self.isValidMove(ind):
                yield(ind)

        for ind in isOnLeft(self.coord):
            if self.isValidMove(ind):
                yield(ind)

    def isValidMove(self, square):
        if not self.isValidSquare(square):
                return INVALID

        if isObtuse(self.coord, square):
            if self.isBlockedOnLeft(self.coord, square):
                return INVALID

            return VALID

        if isAcute(self.coord, square):
            if self.isBlockedOnRight(self.coord, square):
                return INVALID

            return VALID

        return INVALID

    def isBlockedOnLeft(self, square1, square2):
        for x, y in goOnLeft(square1, square2):
            if self.board[x][y]:
                return True

        return False

    def isBlockedOnRight(self, square1, square2):
        for x, y in goOnRight(square1, square2):
            if self.board[x][y]:
                return True

        return False


class Knight(Piece):
    def __init__(self, board, color, coord):
        Piece.__init__(self, board, color, coord)
        self.type = 'knight'

    def pieceReach(self):
        for ind in vertice(self.coord):
            if self.isValidMove(ind):
                yield(ind)


    def isValidMove(self, square):
        if not self.isValidSquare(square):
            return INVALID
       
        for ind in vertice(self.coord):
            if ind == square:
                return VALID

        return INVALID
        
class Rook(Piece):
    def __init__(self, board, color, coord):
        Piece.__init__(self, board, color, coord)
        self.type = 'rook'

    def pieceReach(self):
        for ind in isOnVertical(self.coord):
            if self.isValidMove(ind):
                yield(ind)

        for ind in isOnHorizontal(self.coord):
            if self.isValidMove(ind):
                yield(ind)

    def isValidMove(self, square):
        if not self.isValidSquare(square):
            return INVALID
   

        if isVertical(self.coord, square):
            if self.isBlockedOnVertical(self.coord, square):
                return INVALID

            return VALID

        if isHorizontal(self.coord, square):
            if self.isBlockedOnHorizontal(self.coord, square):
                return INVALID
            return VALID

        return INVALID

    def isBlockedOnHorizontal(self, square1, square2):
        for x, y in goOnHorizontal(square1, square2):
            if self.board[x][y]:
                return True

        return False

    def isBlockedOnVertical(self, square1, square2):
        for x, y in goOnVertical(square1, square2):
            if self.board[x][y]:
                return True
        return False


class Queen(Bishop, Rook):
    def __init__(self, board, color, coord):
        Piece.__init__(self, board, color, coord)
        self.type = 'queen'

    def pieceReach(self):
        for ind in Bishop.pieceReach(self):
            yield(ind)

        for ind in Rook.pieceReach(self):
            yield(ind)

    def isValidMove(self, square):
        if not self.isValidSquare(square):
            return INVALID
       
        alpha = Bishop.isValidMove(self, square)
        beta  = Rook.isValidMove(self, square)

        if alpha or beta:
            return VALID
        
        return INVALID

class Pawn(Rook):
    def __init__(self, board, color, coord):
        Piece.__init__(self, board, color, coord)
        self.type = 'pawn'

    def oppositeSide(self):
        if self.color == WHITE:
            return -1
        else:
            return 1

    def pieceReach(self):
        side = self.oppositeSide()

        for ind in arrow(side, self.coord):
            code = self.isValidMove(ind)
            if code:
                yield(ind)

    def firstCaseEnPasant(self, square):
        x1, y1 = self.coord
        x2, y2 = square

        side = self.oppositeSide()

        if y2 == y1 - 1 and x2 == x1 + side:
            left = self.board[x1][y1 - 1]

            if not left:
                return False

            if not isinstance(left, Pawn):
                return False

            if left.isOppositeColor(self.coord):
                if left.count == 1:
                    return True

        return False

    def secondCaseEnPasant(self, square):
        x1, y1 = self.coord
        x2, y2 = square

        side = self.oppositeSide()

        if y2 == y1 + 1 and x2 == x1 + side:
            right = self.board[x1][y1 + 1]

            if not right:
                return False

            if not isinstance(right, Pawn):
                return False

            if right.isOppositeColor(self.coord):
                if right.count == 1:
                    return True

        return False



    def isEnPasant(self, square):
        alpha = self.firstCaseEnPasant(square)
        beta = self.secondCaseEnPasant(square)

        if alpha or beta:
            last = self.board.lastMove()

            m, n = last

            xn, yn = n

            x1, y1 = self.coord
            x2, y2 = square  

            if (xn, yn) == (x1, y2):
                return True

        return False

    def isTake(self, square):
        x1, y1 = self.coord
        x2, y2 = square

        side = self.oppositeSide()
        if x2 != x1 + side:
            return False

        if y2 != y1 - 1 and y2 != y1 + 1:
            return False

        if not self.board[x2][y2]:
            return False

        return True

    def isNormalMove(self, square):
        x1, y1 = self.coord
        x2, y2 = square

        if self.board[x2][y2]:
            return False

        side = self.oppositeSide()

        if y1 != y2:
            return False

        if x2 == x1 + side:
            return True

        if x2 == x1 + 2 * side:
            if not self.count:
                return True

        return False

    def isPromotion(self, square):
        if not self.isNormalMove(square) and not self.isTake(square):
            return False

        x2, y2 = square

        if x2 == 0 or x2 == 7:
            return True

        return False

    def isValidMove(self, square):
        if not self.isValidSquare(square):
            return INVALID

        if self.isPromotion(square):
            return PROMOTION
        elif self.isNormalMove(square):
            return VALID
        elif self.isTake(square):
            return VALID
        elif self.isEnPasant(square):
                return ENPASANT
        
        return INVALID

    
class King(Piece):
    def __init__(self, board, color, coord):
        Piece.__init__(self, board, color, coord)
        self.type = 'king'

    def isFreeKingSide(self):
        x1, y1 = self.coord

        if self.board[x1][y1 + 1]:
            return False

        if self.board[x1][y1 + 2]:
            return False

        return True

    def isFreeQueenSide(self):
        x1, y1 = self.coord

        if self.board[x1][y1 - 1]:
            return False

        if self.board[x1][y1 - 2]:
            return False
        
        if self.board[x1][y1 - 3]:
            return False
        
        return True

    def isThreatenedKingSide(self, square):
        x1, y1 = self.coord

        m = (x1, y1 + 1)
        n = (x1, y1 + 2)
        color = self.oppositeColor()

        for indi in self.board.matter(color):
            for indj in indi.pieceReach():
                if indj == self.coord:
                    return True

                if indj == m:
                    return True
                if indj == n:
                    return True
        return False

    def isThreatenedQueenSide(self, square):
        x1, y1 = self.coord

        m = (x1, y1 - 1)
        n = (x1, y1 - 2)
        e = (x1, y1 - 3)

        color = self.oppositeColor()

        for indi in self.board.matter(color):
            for indj in indi.pieceReach():
                if indj == self.coord:
                    return True

                if indj == m:
                    return True
                if indj == n:
                    return True

                if indj == e:
                    return True

        return False


    def isKingCastle(self, square):
        if self.count:
            return False

        
        if not self.isFreeKingSide():
            return False

        if self.isThreatenedKingSide(square):
            return False


        if square != (7, 6) and square != (0, 6):
            return False

        x, y = square

               
        item = self.board[x][y + 1]

        if not item:
            return False

        if not isinstance(item, Rook):
            return False

        if item.color != self.color:
            return False

        if item.count:
            return False

        return True

    def isQueenCastle(self, square):
        if self.count:
            return False

        if not self.isFreeQueenSide():
            return False

        if self.isThreatenedQueenSide(square):
            return False


        if square != (0, 2) and square != (7, 2):
            return False

        x, y = square

        item = self.board[x][y - 2]

        if not item:
            return False

        if not isinstance(item, Rook):
            return False

        if item.color != self.color:
            return False

        if item.count:
            return False

        return True


    def isNormalMove(self, square):
        if not self.isValidSquare(square):
            return False
 
        for ind in edge(self.coord):
            if ind == square:
                return True

        return False

    def pieceReach(self):
        """ Returns all the surrounding squares differing from color """

        for x, y in edge(self.coord):
            """ I can't use self.isValidMove here otherwise 
                we ould have a infinite recursion since i'm using pieceReach in 
                King.isValidMove
            """

            if not self.board[x][y]:
                yield((x, y))
                continue

            if self.isOppositeColor((x, y)):
                yield((x,y))

    def isValidMove(self, square):
        if self.isNormalMove(square):
            return VALID
        elif self.isKingCastle(square):
            return KING_CASTLE
        elif self.isQueenCastle(square):
            return QUEEN_CASTLE
        return INVALID
