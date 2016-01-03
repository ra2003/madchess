from Tkinter import *


class ShowTime(Label):
    def __init__(self, count=0,  **args):
        Label.__init__(self, **args)
        self.count = count
        self.setTime(count)
        self.data = []


    def format(self, time):
        hour = time / 60 ** 2
        min = (time - hour * 60 ** 2) / 60
        sec = time - (hour * 60 ** 2 + min * 60) 

        return hour, min, sec


    def inc(self, count):
        self.count = self.count + count
        self.setTime(self.count)

    def dec(self, count):
        self.count = self.count - count
        self.setTime(self.count)

    def setTime(self, count):
        self.count = count

        formated = self.format(self.count)

        data = '%02d:%02d:%02d' % formated 

        self.configure(text=data)

    def getTime(self):
        return self.count


class GClock(Frame):
    def __init__(self, root, **kwargs):
        Frame.__init__(self, master=root, board=None, game=None, **kwargs)

        self.root = root

        self.img1  = PhotoImage(file='img/black/pawn.gif')
        self.img2  = PhotoImage(file='img/white/pawn.gif')
        self.top = Frame(self)
        self.down = Frame(self)

        self.label1 = Label(master=self.top, 
                           anchor=E,
                           text='Black', 
                           image=self.img1)

        self.label2 = Label(master=self.down, 
                           anchor=E,
                           text='White',
                           image=self.img2)

        self.label3 = ShowTime(master=self.top,
                               anchor=W,
                               font=('Helvetica', 40))

        self.label4 = ShowTime(master= self.down, 
                               anchor=W,
                               font=('Helvetica', 40))

        self.top.pack(side='top', expand=True, fill=BOTH)
        self.down.pack(side='top', expand=True, fill=BOTH)
        self.label1.pack(side='left', expand=True, fill=BOTH)
        self.label3.pack(side='left', expand=True, fill=BOTH)
        self.label2.pack(side='left', expand=True, fill=BOTH)
        self.label4.pack(side='left', expand=True, fill=BOTH)

        self.blink = self.label4

        self.running = False

    def back(self):
        time2 = self.data.pop()
        time1 = self.data.pop()

        self.label3.setTime(time1)
        self.label4.setTime(time2)

        if self.blink == self.label3:
            self.blink = self.label4
        else:
            self.blink = self.label3


    def reset(self, time):
        self.data = []
        self.blink = self.label4
        self.label3.setTime(time)
        self.label4.setTime(time)

    def updateTime(self):
        if not self.running:
            return

        self.root.after(1000, self.updateTime)

        self.blink.dec(1)

        count = self.blink.getTime()

        """ i have to implement the increment """
        if not count:
            self.stop()
            self.event_generate('<<zero>>')

    def start(self):
        self.running = True
        self.data.append(self.label3.getTime())
        self.data.append(self.label4.getTime())
        self.updateTime()

    def stop(self):
        self.running = False

    def invert(self):
        if not self.running:
            self.start()

        if self.blink == self.label3:
            self.blink = self.label4
        else:
            self.blink = self.label3

        self.data.append(self.label3.getTime())
        self.data.append(self.label4.getTime())

    def fixTime(self, time):
        pass



if __name__ == '__main__':
    app = Tk()
    alpha = GClock(app)
    alpha.reset(60)
    alpha.start()
    alpha.pack()
    app.mainloop()
