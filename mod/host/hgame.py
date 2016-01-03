from utils import buf
import socket
from mate.board import *
from mod.utils.game import *

import re

NEW_MATCH = 1
MATCH_ACCEPTED = 2
MATCH_REFUSED  = 3
TAKE_ONE_BACK = 4
TAKE_ONE_BACK_REFUSED = 5
TAKE_TWO_BACK = 6
TAKE_TWO_BACK_REFUSED = 7
RESIGN = 8
DRAW = 9
HOST_DISCONNECTED = 10
TIME_IS_OVER = 11
NEW_MSG = 12
NEW_MOVE = 13
GAME_IS_OVER = 14
NOT_CONNECTED = 15
HOST_CONNECTED = 16
ACCEPTED_CONNECTION = 17
TAKE_ONE_BACK_ACCEPTED = 18
TAKE_TWO_BACK_ACCEPTED = 19

class Chat(object):
    def __init__(self, pool, nick):
        self.pool = pool
        self.nick = nick
        self.data = []
    
    def sendMsg(self, text):
        msg = '<%s> %s' % (self.nick, text)
        self.data.append(msg)

        header = ':msg %s\n' % msg
        self.pool.send(header)

    """ updateChat(self, msg) """
    def updateChat(self):
        header = self.pool.queue[0]

        web = re.match(':msg (?P<msg>.*)', header)

        if not web:
            return

        msg = web.group('msg')
        self.data.append('%s\n' % msg)

        del self.pool.queue[0]

    def readData(self):
        return self.data

    def lastMsg(self):
        return self.data[-1]

class HGame(Game):
    def __init__(self, pool):
        Game.__init__(self)
        self.pool = pool
        """i will not need to call it cause the LGame will have a lock"""

    def reset(self, hostColor=None, localColor=None, time=0):
        opposite = lambda x: WHITE if x == BLACK else BLACK
        """this will not be needed either """

        if hostColor:
            self.localColor = opposite(hostColor)
        elif localColor:
            self.localColor = localColor

        Game.reset(self)

    """localMove(self, square1, square2) """
    def localMove(self, code, square1, square2, choice):
        m, n = square1
        e, d = square2
        item = self.board[m][n]

        if not item:
            return INVALID


        if item.color != self.localColor:
            return INVALID

        """i need to test whether it is needed """

        code = self.board.move(code, square1, square2, choice)

        if code == INVALID:
            return INVALID

        self.pool.send(':move %s %s %s %s %s\n' % (m, n, e, d, choice))

        return code

    def takeOneBack(self):
        pass

    def takeTwoBack(self):
        pass

    def acceptTakeOneBack(self):
        pass

    def acceptTakeTwoBack(self):
        pass

    def resign(self):
        pass

    def draw(self):
        pass

    def acceptDraw(self):
        pass

    def abort(self):
        pass

    def unpackMove(self):
        data = self.pool.queue[0]

        web = re.match(':move (?P<s1>.*) (?P<s2>.*) (?P<e1>.*) (?P<e2>.*) (?P<c>.*)', data)

        if not web:
            return

        s1 = int(web.group('s1'))
        s2 = int(web.group('s2'))
        e1 = int(web.group('e1'))
        e2 = int(web.group('e2'))
        c = web.group('c')

        """ it lacks finishing """

        del self.pool.queue[0]

        return ((s1, s2), (e1, e2), c)

    def hostMove(self):
        """
        opposite = lambda x: WHITE if x == BLACK else WHITE

        if self.lockBoard:
            return INVALID

        m, n = self.unpackMove()
        x, y = square1
        e, d = square2

        item = self.board[x][y]

        otherSide = opposite(item.color)

        if self.lockSide == otherSide:
            return INVALID
        """

        m, n, c = self.unpackMove()

        code = self.board.ruler.eval(m, n)

        self.board.move(code, m, n, c)

        return (code, m, n, c)

def Observer(object):
    pass

class Host(object):
    def __init__(self):
        self.connected = False
        self.waiting = False

    def connect(self, host, port, nick):
        if self.connected:
            self.disconnect()

        self.nick = nick
        sock = socket.create_connection((host, port))
        self.pool = buf.Buf(sock)
        self.connected = True
        self.chat = Chat(self.pool, self.nick)
        self.pool.send(':host connected\n')
        self.hostaddr = host
        self.game = HGame(self.pool)
        self.connected = True

    def hostConnected(self):
        del self.pool.queue[0]
        self.game = HGame(self.pool)
        self.pool.send(':accepted connection\n')
        self.connected = True
        self.waiting = False

    def disconnect(self):
        if self.connected:
            self.pool.send(':host disconnected\n')
            self.pool.down()
            self.connected = False

        if self.waiting:
            self.alpha.down()
            self.waiting = False

    def hostDisconnected(self):
        del self.pool.queue[0]
        self.pool.down()
        self.connected = False

    def acceptedConnection(self):
        del self.pool.queue[0]

    def newMatch(self, color, time):
        self.opt = (color, time)
        self.pool.send(':new match %s %s\n' % (color, time))

    def server(self, host, port, nick):
        self.nick = nick
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))

        sock.listen(1)
        self.waiting = True
        self.alpha = buf.accept(sock, self.handleConnect, 1)
        
        """ verify whether the host matches """

    def handleConnect(self, info):
        hostsock, addr = info
       
        """ i have to improve it """
        self.hostaddr = addr[0]

        self.pool = buf.Buf(hostsock)
        self.chat = Chat(self.pool, self.nick)
        self.connected = True
        print 'connected:', hostsock, addr

    def observe(self, host, port):
        pass

    def acceptMatch(self):
        content = self.pool.queue.popleft()

        web = re.match(':new match (?P<color>.*) (?P<time>.*)', content)

        if not web:
            return

        color = int(web.group('color'))
        time = int(web.group('time'))

        self.game.reset(hostColor=color, time=time)

        self.pool.send(':match accepted\n')

        return color, time

    def refuseMatch(self):
        del self.pool.queue[0]
        self.pool.send(':match refused\n')

    def acceptedMatch(self):
        color, time = self.opt

        self.game.reset(localColor=color, time=time)

        del self.pool.queue[0]
        return color, time

    def refusedMatch(self):
        del self.pool.queue[0]


    def sendTakeOneBack(self):
        self.pool.send(':new takeoneback\n')

    def sendTakeTwoBack(self):
        self.pool.send(':new taketwoback\n')


    def acceptTakeOneBack(self):
        del self.pool.queue[0]
        self.pool.send(':takeoneback accepted\n')
        data = self.game.board.back()
        return data

    def acceptTakeTwoBack(self):
        del self.pool.queue[0]
        self.pool.send(':taketwoback accepted\n')
        self.game.board.back()
        data = self.game.board.back()
        return data


    def refuseTakeOneBack(self):
        del self.pool.queue[0]
        self.pool.send(':takeoneback refused\n')

    def refuseTakeTwoBack(self):
        del self.pool.queue[0]
        self.pool.send(':taketwoback refused\n')


    def acceptedTakeOneBack(self):
        del self.pool.queue[0]
        data = self.game.board.back()
        return data

    def acceptedTakeTwoBack(self):
        del self.pool.queue[0]
        self.game.board.back()
        data = self.game.board.back()
        return data


    def refusedTakeOneBack(self):
        del self.pool.queue[0]

    def refusedTakeTwoBack(self):
        del self.pool.queue[0]


    def process(self):
        if not self.connected:
            return NOT_CONNECTED
        
        size = len(self.pool.queue)

        if not size:
            return None

        content = self.pool.queue[0]

        if content.startswith(':new match'):
            return NEW_MATCH
        elif content.startswith(':msg'):
            return NEW_MSG
        elif content.startswith(':move'):
            return NEW_MOVE
        elif content.startswith(':match accepted'):
            return MATCH_ACCEPTED
        elif content.startswith(':match refused'):
            return MATCH_REFUSED
        elif content.startswith(':host disconnected'):
            return HOST_DISCONNECTED
        elif content.startswith(':host connected'):
            return HOST_CONNECTED
        elif content.startswith(':accepted connection'):
            return ACCEPTED_CONNECTION
        elif content.startswith(':new takeoneback'):
            return TAKE_ONE_BACK
        elif content.startswith(':takeoneback accepted'):
            return  TAKE_ONE_BACK_ACCEPTED
        elif content.startswith(':takeoneback refused'):
            return TAKE_ONE_BACK_REFUSED
        elif content.startswith(':new taketwoback'):
            return TAKE_TWO_BACK
        elif content.startswith(':taketwoback accepted'):
            return TAKE_TWO_BACK_ACCEPTED
        elif content.startswith(':taketwoback refused'):
            return TAKE_TWO_BACK_REFUSED

