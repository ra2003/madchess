from Tkinter import *
from mod.utils.game import *
from mod.utils.gmatch import *

class GLocal(object):
    def __init__(self, root, gboard, gclock, gmove):
        self.root = root
        self.gboard = gboard
        self.gclock = gclock
        self.gmove = gmove

        self.game = Game()


        self.img1 = PhotoImage(file='icon/NewGame.gif')
        self.img2 = PhotoImage(file='icon/TakeOneBack.gif')
        self.img3 = PhotoImage(file='icon/TakeTwoBack.gif')
        self.img4 = PhotoImage(file='icon/Resign.gif')
        self.img5 = PhotoImage(file='icon/Draw.gif')
        self.img6 = PhotoImage(file='icon/Abort.gif')


        self.button1 = Button(master=self.root, text='New game',
                              image=self.img1,
                              command=self.newGame)


        self.button2 = Button(master=self.root, text='Take once back', 
                                  image=self.img2,
                                  command=self.takeOneBack)

        self.button3 = Button(master=self.root, text='Take twice back',
                                  image=self.img3,
                                  command=self.takeTwoBack)

        """
        self.button4 = Button(master=self.root, text='Resign', image=self.img4)
        self.button5 = Button(master=self.root, text='Draw', image=self.img5)
        self.button6 = Button(master=self.root, text='Abort', image=self.img6)
        """

        self.button1.grid(row=0, column=0, sticky=W+E+N+S)
        self.button2.grid(row=0, column=1, sticky=W+E+N+S)
        self.button3.grid(row=0, column=2, sticky=W+E+N+S)
        """
        self.button4.grid(row=1, column=0, sticky=W+E+N+S)
        self.button5.grid(row=1, column=1, sticky=W+E+N+S)
        self.button6.grid(row=1, column=2, sticky=W+E+N+S)
        """

        """ Starting a new game """
        #self.button1.invoke()

    def finish(self):
        self.gboard.setBreaker(None)
        self.gboard.setRuler(None)

    def newGame(self):
        alpha = GMatch(self.root)

        if not alpha.info:
            return

        self.gboard.setBreaker(self.game.move)
        self.gboard.setRuler(self.game.board.ruler.eval)
        self.gboard.base = self.game.board.ruler
        self.game.reset()
        self.gboard.reset()
        self.gmove.reset()

        opt, time  = alpha.info

        self.gclock.reset(time)

    def takeOneBack(self):
        state = self.game.board.back()
        self.gboard.redraw(state)
        self.gclock.back()

    def takeTwoBack(self):
        self.game.board.back()
        state = self.game.board.back()
        self.gboard.redraw(state)

        self.gclock.back()
        self.gclock.back()

    def resign(self):
        pass

    def drawButton(self):
        pass

    def abort(self):
        pass


