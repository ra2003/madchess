from socket import *

def prepare():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('0.0.0.0', 8080))
    return sock
