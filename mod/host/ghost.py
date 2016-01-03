from Tkinter import *
from gchat import *
from tkSimpleDialog import askstring, askinteger
from tkMessageBox import askyesno, showwarning, showinfo
from gask import *
from hgame import *
from mod.utils.gmatch import *

class GHost(object):
    def __init__(self, root, gboard=None, gclock=None, gmove=None):
        self.root = root

        self.gclock = gclock
        self.gboard = gboard
        self.gmove = gmove

        self.gchat = None
        self.running = False

        self.host = Host() 

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
                                  image=self.img6, command=self.sendTakeOneBack)

        self.button7 = Button(master=self.root, text='Take twice back',
                                  image=self.img7, command=self.sendTakeTwoBack)

        """
        self.button8 = Button(master=self.root, text='Resign', image=self.img8)
        self.button9 = Button(master=self.root, text='Draw', image=self.img9)
        self.button10 = Button(master=self.root, text='Abort', image=self.img10)
        """

        self.button1.grid(row=0, column=0, sticky=W+E+N+S)
        self.button2.grid(row=0, column=1, sticky=W+E+N+S)
        self.button3.grid(row=0, column=2, sticky=W+E+N+S)
        self.button4.grid(row=0, column=3, sticky=W+E+N+S)
        self.button5.grid(row=1, column=0, sticky=W+E+N+S)
        self.button6.grid(row=1, column=1, sticky=W+E+N+S)
        self.button7.grid(row=1, column=2, sticky=W+E+N+S)
        """
        self.button8.grid(row=2, column=0, sticky=W+E+N+S)
        self.button9.grid(row=2, column=1, sticky=W+E+N+S)
        self.button10.grid(row=2, column=2, sticky=W+E+N+S)
        """

    def finish(self):
        self.disconnect()

    def connect(self):
        dial = GAsk(self.root)

        opt = dial.get()

        if not opt:
            return

        ip, port, nick = opt

        try:
            self.host.connect(ip, port, nick)
            self.running = True
            self.caller()
        except:
            showinfo('Information', 'Connection was refused !')

    def newGame(self):
        """
        color = lambda x: 12 if x == 'white' else 13
        reply = askstring('Color', 'What color ?')

        side = color(reply)
        
        time = 0
        """
        alpha = GMatch(self.root)
        
        if alpha.info == None:
            return

        opt, time = alpha.info

        self.host.newMatch(opt, time)


    def disconnect(self):
        if not self.running:
            return

        self.running = False
        self.host.disconnect()
   
    def sendTakeOneBack(self):
        self.host.sendTakeOneBack()

    def sendTakeTwoBack(self):
        self.host.sendTakeTwoBack()


    def hostConnected(self):
        self.host.hostConnected()

        #showinfo('Host info', 'Host connected: %s' % str(self.host.hostaddr))

        self.initializeChat()

    def acceptedConnection(self):
        self.host.acceptedConnection()

        #showinfo('Connection', 'Host accepted connection: %s' % str(self.host.hostaddr))

        self.initializeChat()

    def hostDisconnected(self):
        self.host.hostDisconnected()
        self.running = False
        showinfo('Host info', 'Host disconnected: %s' % str(self.host.hostaddr))

    def initializeChat(self):
        self.gchat = GChat(self.root, self.host.chat.sendMsg, self.host.chat.nick)
        self.gchat.protocol('WM_DELETE_WINDOW', lambda x=self.gchat: x.withdraw())

        text = ''.join(self.host.chat.data)

        self.gchat.update(text)

    def showChat(self):
        if not self.running:
            return

        self.gchat.wm_deiconify()

    def server(self):
        dial = GAsk(self.root)

        opt = dial.get()

        if not opt:
            return

        ip, port, nick = opt

        self.host.server(ip, port, nick)
        self.running = True
        self.caller()


    def issuedMatch(self):
        info = self.host.pool.queue[0]

        ok = askyesno('Challenge', 
                      'There is a challenge %s!' % str(info))

        if ok:
            self.acceptMatch()
        else:
            self.refuseMatch()

    def acceptMatch(self):
        color, time = self.host.acceptMatch()

        self.gclock.reset(time)

        self.gboard.reset()
        self.gmove.reset()

        self.gboard.setRuler(self.host.game.board.ruler.eval)
        self.gboard.setBreaker(self.host.game.localMove)
        self.gboard.base = self.host.game.board.ruler

    def refuseMatch(self):
        self.host.refuseMatch()
        showinfo('Match', 'Refusing match !')

    def refusedMatch(self):
        self.host.refusedMatch()
        showinfo('Match', 'The match was refused')

    def acceptedMatch(self):
        color, time = self.host.acceptedMatch()

        self.gclock.reset(time)

        self.gboard.reset()
        self.gmove.reset()

        self.gboard.setRuler(self.host.game.board.ruler.eval)
        self.gboard.setBreaker(self.host.game.localMove)
        self.gboard.base = self.host.game.board.ruler

    def issuedTakeOneBack(self):
        info = self.host.pool.queue[0]

        ok = askyesno('Challenge', 
                      'Your opponent requested a take one back ! Accept it?')

        if ok:
            self.acceptTakeOneBack()
        else:
            self.refuseTakeOneBack()

    def issuedTakeTwoBack(self):
        info = self.host.pool.queue[0]

        ok = askyesno('Challenge', 
                      'Your opponent requested a take two back ! Accept it?')

        if ok:
            self.acceptTakeTwoBack()
        else:
            self.refuseTakeTwoBack()


    def acceptTakeOneBack(self):
        data = self.host.acceptTakeOneBack()
        self.gboard.redraw(data)
        self.gclock.back()

    def acceptTakeTwoBack(self):
        data = self.host.acceptTakeTwoBack()
        self.gboard.redraw(data)
        self.gclock.back()
        self.gclock.back()

    def refuseTakeOneBack(self):
        self.host.refuseTakeOneBack()

    def refuseTakeTwoBack(self):
        self.host.refuseTakeTwoBack()


    def acceptedTakeOneBack(self):
        data = self.host.acceptedTakeOneBack()
        self.gboard.redraw(data)
        self.gclock.back()
        pass

    def acceptedTakeTwoBack(self):
        data = self.host.acceptedTakeTwoBack()
        self.gboard.redraw(data)
        self.gclock.back()
        self.gclock.back()
        pass


    def refusedTakeOneBack(self):
        self.host.refusedTakeOneBack()
        showinfo('Match', 'The take one back was refused !')

    def refusedTakeTwoBack(self):
        self.host.refusedTakeTwoBack()
        showinfo('Match', 'The take two back was refused !')


    def caller(self):
        if not self.running:
            return
    
        self.process()
        self.root.after(200, self.caller)

    def updateBoard(self):
        code, square1, square2, choice = self.host.game.hostMove()

        #square1, square2, choice = self.host.game.board.data[-1]

        print 'updating board', square1, square2

        self.gboard.updateMove(code, square1, square2, choice)

        if code == PROMOTION:
            x1,y1 = square2

            color = self.gboard.base.board[x1][y1].oppositeColor()

            if self.gboard.base.isCheckMate(color):
                self.gboard.event_generate('<<CHECK-MATE>>')

    def updateChat(self):
        if not self.gchat:
            return

        self.host.chat.updateChat()

        text = self.host.chat.data[-1]

        self.gchat.update(text)


    def process(self):
        code = self.host.process()

        if not code:
            return None

        if code == NOT_CONNECTED:
            return code

        if code == NEW_MATCH:
            self.issuedMatch()
        elif code == NEW_MSG:
            self.updateChat()
        elif code == NEW_MOVE:
            self.updateBoard()
        elif code == MATCH_ACCEPTED:
            self.acceptedMatch()
        elif code == MATCH_REFUSED:
            print 'MATCH REFUSED'
            self.refusedMatch()
        elif code == HOST_DISCONNECTED:
            print 'HOST DISCONNECTED'
            self.hostDisconnected()
        elif code == HOST_CONNECTED:
            self.hostConnected()
        elif code == ACCEPTED_CONNECTION:
            self.acceptedConnection()
        elif code == TAKE_ONE_BACK:
            self.issuedTakeOneBack()
        elif code == TAKE_ONE_BACK_ACCEPTED:
            self.acceptedTakeOneBack()
        elif code == TAKE_ONE_BACK_REFUSED:
            self.refusedTakeOneBack()
        elif code == TAKE_TWO_BACK:
            self.issuedTakeTwoBack()
        elif code == TAKE_TWO_BACK_ACCEPTED:
            self.acceptedTakeTwoBack()
        elif code == TAKE_TWO_BACK_REFUSED:
            self.refusedTakeTwoBack()


        return code
        

