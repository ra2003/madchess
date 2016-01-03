from ruler import *

class Board(list):
    def __init__(self, initial=None):
        list.__init__(self)
        self.ruler = Ruler(self)

        for indi in xrange(0, 8):
            row = []

            for indj in xrange(0, 8):
                row.append(None)

            self.append(row)

        
        self.reset()

    
    def reset(self):
        """verify whether it is being used """
        self.stack = []
        self.data = []
        self.count = 0
        self.player = WHITE

        size = len(self)
        for indi in xrange(0, 8):
            for indj in xrange(0, 8):
                self[indi][indj] = None

    def clear(self):
        l = len(self)
        for ind in xrange(0, l):
            self.pop()

    def matter(self, color):
        for indi in self:
            for indj in indi:
                if indj:
                    if indj.color == color:
                        yield(indj)


    def lastMove(self):
        if not self.data:
            return None

        return self.data[-1]

    def findPiece(self, type, color):
        for indi in self:
            for indj in indi:
                if indj:
                    if indj.type == type and indj.color == color:
                        yield(indj)

    
    def case(self, square1, square2):
        x1, y1 = square1

        code = self[x1][y1].isValidMove(square2)
        return self.updateMove(code, square1, square2)

    def updateMove(self, code, square1, square2, choice='Pawn'):
        x1, y1 = square1

        x2, y2 = square2

        mp1 = self[x1][y1]
        mp2 = self[x2][y2]

        self.data.append((square1, square2))
        self[x2][y2] = self[x1][y1]
        self[x2][y2].coord = (x2, y2)
        self[x1][y1] = None
        self[x2][y2].count = self[x2][y2].count + 1

        if code == ENPASANT:
            mp3 = self[x1][y2]
            self[x1][y2] = None

        if code == KING_CASTLE:
            self[x2][y2 + 1].count = self[x2][y2 + 1].count + 1
            self[x2][y2 - 1] = self[x2][y2 + 1]
            self[x2][y2 - 1].coord = (x2, y2 - 1)
            self[x2][y2 + 1] = None

        if code == QUEEN_CASTLE:
            self[x2][y2 - 2].count = self[x2][y2 - 2].count + 1
            self[x2][y2 + 1] = self[x2][y2 - 2]
            self[x2][y2 + 1].coord = (x2, y2 + 1)

            self[x2][y2 - 2] = None

        if code == PROMOTION:
            new = globals()[choice]
            self[x2][y2] = new(self, self[x2][y2].color, (x2, y2))

        self.invertPlayer()

        yield

        self.data.pop()
        self[x1][y1] = mp1
        self[x2][y2] = mp2
        self[x1][y1].count = self[x1][y1].count - 1 

        if self[x1][y1]:
            self[x1][y1].coord = (x1, y1)
       
        if code == ENPASANT:
           self[x1][y2] = mp3

        if code == KING_CASTLE:
            self[x2][y2 + 1] = self[x2][y2 - 1]
            self[x2][y2 - 1] = None
            self[x2][y2 + 1].coord = (x2, y2 + 1)
            self[x2][y2 + 1].count = self[x2][y2 + 1].count - 1

        if code == QUEEN_CASTLE:
            self[x2][y2 - 2] = self[x2][y2 + 1]
            self[x2][y2 - 2].count = self[x2][y2 - 2].count - 1
            self[x2][y2 - 2].coord = (x2, y2 - 2)

            self[x2][y2 + 1] = None

        if code == PROMOTION:
            self[x2][y2] = mp2

        self.invertPlayer()
        yield
      

    def move(self, code,  square1, square2, choice):
        #code = self.ruler.eval(square1, square2)
        
        if code == INVALID:
            return INVALID

        seq = self.updateMove(code, square1, square2, choice)
        seq.next()

        self.stack.append(seq)
        self.count = self.count + 1

        return code

    def invertPlayer(self):
        if self.player == WHITE:
            self.player = BLACK
        else:
            self.player = WHITE


    def back(self):
        state = self.stack.pop()
        state.next()
        self.count = self.count - 1

        return self

    def squareAttack(self, square):
        """ It returns a list with all pieces 
            whose reach achieves square """

        for indi in self:
            for indj in indi:
                if indj:
                    if indj.isValidMove(square):
                        yield(indj)

