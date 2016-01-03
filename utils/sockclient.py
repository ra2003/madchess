from socket import *

def client():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('0.0.0.0', 50007))
    return sock

