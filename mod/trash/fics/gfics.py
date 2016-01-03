from Tkinter import *

class GFics(object):
    def __init__(self, root):
        self.root = root

        self.img1 = PhotoImage(file='icon/Plug.gif')
        self.img2 = PhotoImage(file='icon/UnPlug.gif')
        self.img3 = PhotoImage(file='icon/Console.gif')
        self.img4 = PhotoImage(file='icon/Chat.gif')
        self.img5 = PhotoImage(file='icon/NewGame.gif')
        self.img6 = PhotoImage(file='icon/FindOpponent.gif')
        self.img7 = PhotoImage(file='icon/TakeOneBack.gif')
        self.img8 = PhotoImage(file='icon/TakeTwoBack.gif')
        self.img9 = PhotoImage(file='icon/Resign.gif')
        self.img10 = PhotoImage(file='icon/Draw.gif')
        self.img11 = PhotoImage(file='icon/Abort.gif')

        self.connect = Button(master=self.root, text='Connect',
                              image=self.img1)

        self.disconnect = Button(master=self.root, text='Disconnect',
                                 image=self.img2)

        self.cmdline = Button(master=self.root, text='Console',
                              image=self.img3)

        self.chat = Button(master=self.root, text='Chat', 
                           image=self.img4)

        self.newGame = Button(master=self.root, text='New game',
                              image=self.img5)

        self.findOpponent = Button(master=self.root, text='Find Opponent',
                                   image=self.img6)

        self.takeOneBack = Button(master=self.root, text='Take once back', 
                                  image=self.img7)

        self.takeTwoBack = Button(master=self.root, text='Take twice back',
                                  image=self.img8)

        self.resign = Button(master=self.root, text='Resign', image=self.img9)
        self.draw = Button(master=self.root, text='Draw', image=self.img10)
        self.abort = Button(master=self.root, text='Abort', image=self.img11)
        """
        self.connect.pack(side='top', fill=X)
        self.disconnect.pack(side='top', fill=X)
        self.cmdline.pack(side='top', fill=X)
        self.chat.pack(side='top', fill=X)
        self.newGame.pack(side='top', fill=X)
        self.findOpponent.pack(side='top', fill=X)
        self.takeOneBack.pack(side='top', fill=X)
        self.takeTwoBack.pack(side='top', fill=X)
        self.resign.pack(side='top', fill=X)
        self.draw.pack(side='top', fill=X)
        self.abort.pack(side='top', fill=X)
        """

        self.connect.grid(row=0, column=0, sticky=W+E+N+S)
        self.disconnect.grid(row=0, column=1, sticky=W+E+N+S)
        self.cmdline.grid(row=0, column=2, sticky=W+E+N+S)
        self.chat.grid(row=1, column=0, sticky=W+E+N+S)
        self.newGame.grid(row=1, column=1, sticky=W+E+N+S)
        self.findOpponent.grid(row=1, column=2, sticky=W+E+N+S)
        self.takeOneBack.grid(row=2, column=0, sticky=W+E+N+S)
        self.takeTwoBack.grid(row=2, column=1, sticky=W+E+N+S)
        self.resign.grid(row=2, column=2, sticky=W+E+N+S)
        self.draw.grid(row=3, column=0, sticky=W+E+N+S)
        self.abort.grid(row=3, column=1, sticky=W+E+N+S)


    def finish(self):
        pass

