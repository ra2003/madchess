class ChessNet(object):
    def __init__(self, sock, 
                       schedule, 
                       period=2000,
                       handleMove=lambda square1, square2: 1,
                       handleText=lambda text: 1):

        self.sock = sock
        self.fd = sock.makefile()
        self.sched = schedule
        self.period = period
        self.running = True
        self.handleMove = handleMove
        self.handleText = handleText
        self.handle()

    def handle(self):
        if not self.running:
            return

        self.sched(self.period, self.handle)
        self.process()

    def sendMove(self, square1, square2):
        pass

    def sendText(self, text):
        self.fd.write(text)
        pass

    def process(self):
        data = self.sock.recv(100)

        if data:
            self.handleText(data)

    def handleMove(self, square1, square2):
        pass

    def handleText(self, text):
        pass

    def stop(self):
        self.running = False
        pass



