from socket import *

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('0.0.0.0', 50007))
    sock.listen(1)
    host, addr = sock.accept()
    return host, addr



