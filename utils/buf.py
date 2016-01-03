from threading import *
from collections import deque
import socket
#from socket import *

class Buf(Thread):
    def __init__(self, sock):
        self.sock = sock
        self.sock.settimeout(3)
        self.fd = sock.makefile(mode='r+')
        #self.fd.settimeout(3)
        self.running = True 
        self.queue = deque()
        Thread.__init__(self)
        self.start()

    def send(self, data):
        self.fd.write(data)
        self.fd.flush()

    def run(self):
        while self.running:
            try:
                data = self.fd.readline()
            except:
                continue

            self.queue.append(data)

        self.fd.close()
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

    def down(self):
        self.running = False
        #self.fd.close()
        #self.sock.close()


class accept(Thread):
    def __init__(self, sock, callback, nhost, *args, **kwargs):
        """i have to close the socket"""
        self.sock = sock
        self.sock.settimeout(3)
        self.handle = (callback, args, kwargs)
        self.nhost = nhost
        self.stack = []
        self.running = True
        Thread.__init__(self)
        self.start()

    def run(self):
        while self.running and self.nhost > 0:
            try:
                host, addr = self.sock.accept()
            except:
                continue

            fmap, args, kwargs = self.handle
            self.stack.append((host, addr))
            fmap((host, addr), *args, **kwargs)
            self.nhost = self.nhost - 1

        self.sock.close()

    def down(self):
        self.running = False

"""
def call(host, *args, **kwargs):
    print host, args, kwargs

def xtest():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('0.0.0.0', 50007))
    sock.listen(3)
    alpha = accept(sock, call, 3, 'i got', data='yeah')
    return alpha
"""
