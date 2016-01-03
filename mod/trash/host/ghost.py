from Tkinter import *
from gchat import *
from tkSimpleDialog import askstring, askinteger
from tkMessageBox import askyesno, showwarning, showinfo
from gask import *

class GHost(object):
    def __init__(self, root, gboard=None):
        self.root = root

        self.gboard = gboard
        self.gchat = None
        self.running = False

        self.host = None

        self.img1 = PhotoImage(master=self.root, file='icon/Plug.gif')
        self.img2 = PhotoImage(master=self.root, file='icon/UnPlug.gif')
        self.img3 = PhotoImage(master=self.root, file='icon/NewPlug.gif')
        self.img4 = PhotoImage(master=self.root, file='icon/Chat.gif')
        self.img5 = PhotoImage(master=self.root, file='icon/NewGame.gif')
        self.img6 = PhotoImage(master=self.root, file='icon/TakeOneBack.gif')
        self.img7 = PhotoImage(master=self.root, file='icon/TakeTwoBack.gif')
        self.img8 = PhotoImage(master=self.root, file='icon/Resign.gif')
        self.img9 = PhotoImage(master=self.root, file='icon/Draw.gif')
        self.img10 = PhotoImage(master=self.root, file='icon/Abort.gif')

        self.button1 = Button(master=self.root, text='Connect',
                              image=self.img1, command=self.connect)

        self.button2 = Button(master=self.root, text='Disconnect',
                                 image=self.img2, command=self.disconnect)


        self.button3 = Button(master=self.root, text='Server', 
                              image=self.img3, command=self.server)

        self.button4 = Button(master=self.root, text='Chat', 
                           image=self.img4, command=self.showChat)

        self.button5 = Button(master=self.root, text='New game',
                              image=self.img5, command=self.newGame)


        self.button6 = Button(master=self.root, text='Take once back', 
                                  image=self.img6)

        self.button7 = Button(master=self.root, text='Take twice back',
                                  image=self.img7)

        self.button8 = Button(master=self.root, text='Resign', image=self.img8)
        self.button9 = Button(master=self.root, text='Draw', image=self.img9)
        self.button10 = Button(master=self.root, text='Abort', image=self.img10)

        self.button1.grid(row=0, column=0, sticky=W+E+N+S)
        self.button2.grid(row=0, column=1, sticky=W+E+N+S)
        self.button3.grid(row=0, column=2, sticky=W+E+N+S)
        self.button4.grid(row=0, column=3, sticky=W+E+N+S)
        self.button5.grid(row=1, column=0, sticky=W+E+N+S)
        self.button6.grid(row=1, column=1, sticky=W+E+N+S)
        self.button7.grid(row=1, column=2, sticky=W+E+N+S)
        self.button8.grid(row=2, column=0, sticky=W+E+N+S)
        self.button9.grid(row=2, column=1, sticky=W+E+N+S)
        self.button10.grid(row=2, column=2, sticky=W+E+N+S)

    def finish(self):
        pass

    def connect(self):
        dial = GAsk(self.root)

        opt = dial.get()

        if not opt:
            return

        ip, port, nick = opt

    def newGame(self):
        pass

    def disconnect(self):
        pass

    def hostConnected(self):
        pass

    def acceptedConnection(self):
        pass

    def hostDisconnected(self):
        pass

    def initializeChat(self):
        pass

    def showChat(self):
        pass

    def server(self):
        pass

    def updateChat(self):
        pass

    def process(self):
        pass


