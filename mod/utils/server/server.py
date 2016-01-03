import asynchat
import asyncore
import socket
#from mod.utils.game import *

class Player(asynchat.async_chat):
    def __init__(self, game, sock):
        asynchat.async_chat.__init__(self, sock=sock)
        self.ibuffer = ""
        self.set_terminator("\n")

        self.game = game

    def collect_incoming_data(self, data):
        self.ibuffer = self.ibuffer + data

    def newGame(self, *args):
        pass

    def makeMove(self, *args):
        pass

    def found_terminator(self):
        print self.ibuffer

        if self.ibuffer.startswith(':msg'):
            self.user.send(self.ibuffer)
       
        if self.ibuffer.startswith(':match'):
            pass

        if self.ibuffer.startswith(':move'):
            pass

        self.ibuffer = ''



class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(2)

        self.game = None
        self.one = None
        self.two = None


    def synchronize(self):
        print 'Synchronizing ...'
        self.two.send(':synchronized\n')
        self.one.send(':synchronized\n')

    def handle_accept(self):
        pair = self.accept()
        sock, addr = pair

        if pair is None:
            return

        print 'Player from from %s' % repr(addr)

        player = Player(self.game, sock)

        if not self.one:
            self.one = player
            return

        self.two = player
        self.one.user = self.two
        self.two.user = self.one
        self.synchronize()
        self.close()

def initialize():
    server = Server('localhost', 8080)
    asyncore.loop()

initialize()

