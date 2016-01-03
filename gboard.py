from Tkinter import *
from mate.piece import *

from tkSimpleDialog import askstring

class GBoard(Frame):
    """ The graphic board class """

    def __init__(self, root, 
                       breaker=None, 
                       ruler=None,
                       base=None,
                       note=None,
                       statusbar=None,
                       color=('gray', 'brown'), 
                       width=52, 
                       height=52, **args):

        self.statusbar = statusbar
        self.breaker = breaker
        self.ruler  = ruler
        self.base = base
        self.color  = color
        self.width  = width
        self.height = height
        self.root   = root
        self.square = IntVar()
        self.state  = None
        self.bd     = []
        self.pin     = []


        Frame.__init__(self, master=self.root, **args)


        """ Initialize a matrix which contains all the images """
        for indi in xrange(8):
            row = []
            for indj in xrange(8):
                img = PhotoImage(master = self)
                row.append(img)

            self.bd.append(row)


        for indi in xrange(8):
            row = []
            for indj in xrange(8):
                square = Radiobutton(master      = self, 
                                     width       = self.width, 
                                     image       = self.bd[indi][indj],
                                     height      = self.height, 
                                     indicatoron = 0, 
                                     value       = indi * 8 + indj,
                                     command     = lambda m=(indi, indj): self.moveHandle(m),
                                     variable    = self.square,
                                     background  = self.squareColor(indi, indj))


                square.grid(row = indi, column=indj)
                row.append(square)

            self.pin.append(row)

            self.reset()

    def reset(self):
        for indi in self.bd:
            for indj in indi:
                indj.blank()

        self.bd[0][0].configure(file='img/black/rook.gif')
        self.bd[0][1].configure(file='img/black/knight.gif')
        self.bd[0][2].configure(file='img/black/bishop.gif')
        self.bd[0][3].configure(file='img/black/queen.gif')
        self.bd[0][4].configure(file='img/black/king.gif')
        self.bd[0][5].configure(file='img/black/bishop.gif')
        self.bd[0][6].configure(file='img/black/knight.gif')
        self.bd[0][7].configure(file='img/black/rook.gif')
        self.bd[1][0].configure(file='img/black/pawn.gif')
        self.bd[1][1].configure(file='img/black/pawn.gif')
        self.bd[1][2].configure(file='img/black/pawn.gif')
        self.bd[1][3].configure(file='img/black/pawn.gif')
        self.bd[1][4].configure(file='img/black/pawn.gif')
        self.bd[1][5].configure(file='img/black/pawn.gif')
        self.bd[1][6].configure(file='img/black/pawn.gif')
        self.bd[1][7].configure(file='img/black/pawn.gif')

        self.bd[7][0].configure(file='img/white/rook.gif')
        self.bd[7][1].configure(file='img/white/knight.gif')
        self.bd[7][2].configure(file='img/white/bishop.gif')
        self.bd[7][3].configure(file='img/white/queen.gif')
        self.bd[7][4].configure(file='img/white/king.gif')
        self.bd[7][5].configure(file='img/white/bishop.gif')
        self.bd[7][6].configure(file='img/white/knight.gif')
        self.bd[7][7].configure(file='img/white/rook.gif')
        self.bd[6][0].configure(file='img/white/pawn.gif')
        self.bd[6][1].configure(file='img/white/pawn.gif')
        self.bd[6][2].configure(file='img/white/pawn.gif')
        self.bd[6][3].configure(file='img/white/pawn.gif')
        self.bd[6][4].configure(file='img/white/pawn.gif')
        self.bd[6][5].configure(file='img/white/pawn.gif')
        self.bd[6][6].configure(file='img/white/pawn.gif')
        self.bd[6][7].configure(file='img/white/pawn.gif')


    def moveHandle(self, m):
        if not self.state:
            self.state = m
            return

        self.makeMove(self.state, m)
        self.state = None
        self.square.set(None)

    def setBreaker(self, callback):
        self.breaker = callback

    def getBreaker(self):
        return self.breaker

    def setRuler(self, callback):
        self.ruler = callback

    def getRuler(self):
        return self.ruler

    def setNote(self, note):
        self.note = note
        pass

    def getNote(self):
        return self.note

    def makeMove(self, m, n):
        """ verify whether the move is valid """

        if not self.breaker:
            return

        code = self.ruler(m, n)
        self.typeMove(code, m, n)

    def updateMove(self, code, square1, square2, choice=None):
        m, n = square1, square2

        if code == INVALID:
            self.event_generate('<<INVALID-MOVE>>')
            return


        i1, j1 = m
        itemx = self.bd[i1][j1]
        fp = itemx.cget('file')


        i2, j2 = n
        itemz = self.bd[i2][j2]
        itemz.configure(file=fp)


        itemx.configure(file='')
        itemx.blank()


        self.event_generate('<<VALID-MOVE>>')
        self.note(m, n)

        if code == CHECK_MATE:
            self.event_generate('<<CHECK-MATE>>')
        #elif code == CHECK:
        #    self.event_generate('<<CHECK-MATE>>')
        elif code == ENPASANT:
            itemw = self.bd[i1][j2]
            itemw.configure(file='')
            itemw.blank()
            self.event_generate('<<ENPASANT>>')
        elif code == QUEEN_CASTLE:
            itemc = self.bd[i2][j2 - 2]
            ft = itemc.cget('file')
            
            itemr = self.bd[i1][j2 + 1]
            itemr.configure(file=ft)
            
            iteme = self.bd[i1][j2 - 2]

            iteme.blank()

            self.event_generate('<<QUEEN-CASTLE>>')
        elif code == KING_CASTLE:
            itemi = self.bd[i2][j2 + 1]
            ft = itemi.cget('file')

            itemj = self.bd[i1][j2 - 1]
            itemj.configure(file=ft)

            iteml = self.bd[i1][j2 + 1].blank()

            self.event_generate('<<KING-CASTLE>>')
        elif code == PROMOTION:
            color = self.pieceColor(self.bd[i2][j2])

            self.bd[i2][j2].configure(file='img/%s/%s.gif' % (color, choice.lower()))

            self.event_generate('<<PAWN-PROMOTION>>')
            #return

        if code == DRAW:
            self.event_generate('<<DRAW>>')
        
    def typeMove(self, code, m, n):
        choice = 'pawn'

        if code == PROMOTION:
            choice = askstring('Promotion', 'Piece ?')


        step = self.breaker(code, m, n, choice)

        self.updateMove(step, m, n, choice)

        if code == PROMOTION:
            x1,y1 = n

            color = self.base.board[x1][y1].oppositeColor()

            if self.base.isCheckMate(color):
                self.event_generate('<<CHECK-MATE>>')

    def pieceColor(self, item):
        ft = item.cget('file')
        local, color, type = ft.split('/')

        return color

    def squareColor(self, x, y):
        kind = lambda x: x % 2
        
        xcolor, ycolor = self.color

        if kind(x) == kind(y): 
            return xcolor
        
        return ycolor


    def clean(self):
        for indi in self.bd:
            for indj in indi:
                indj.configure(file='')
                indj.blank()

    def redraw(self, data):
        for indi in xrange(8):
            for indj in xrange(8):
                item1 = data[indi][indj]

                item2 = self.bd[indi][indj]

                if item1 == None:
                    item2.configure(file='')
                    item2.blank()
                    continue

                color = 'white' if item1.color == 12 else 'black'
                matter = item1.type

                fp = 'img/%s/%s.gif' % (color, matter)
                item2.configure(file=fp)

    def zoomInBoard(self, rate):
        for indi in self.pin:
            for indj in indi:
                w = indj.cget('width')
                h = indj.cget('height')
                wn = int(str(w)) + rate
                hn = int(str(h)) + rate
                indj.configure(width = wn, height = hn)

    def zoomOutBoard(self, rate):
        for indi in self.pin:
            for indj in indi:
                w = indj.cget('width')
                h = indj.cget('height')
                wn = int(str(w)) - rate
                hn = int(str(h)) - rate
                indj.configure(width = wn, height = hn)



if __name__ == '__main__':
    root = Tk()
    app = GBoard(root)
    root.mainloop()

