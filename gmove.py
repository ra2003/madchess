from Tkinter import *

class GMove(Frame):
    def __init__(self, root, **kwargs):
        self.root = root

        Frame.__init__(self, master=self.root, **kwargs)
        """
        self.img1 = PhotoImage(file='icon/pause.gif')
        self.img2 = PhotoImage(file='icon/start.gif')
        self.img3 = PhotoImage(file='icon/back.gif')
        self.img4 = PhotoImage(file='icon/play.gif')
        self.img5 = PhotoImage(file='icon/foward.gif')
        self.img6 = PhotoImage(file='icon/end.gif')
        """
        self.box   = Listbox(self,relief=GROOVE,border=3, height=5)
        """
        self.pause  = Button(self, text='pause', image=self.img1)
        self.start = Button(self, text='Start', image=self.img2)
        self.back  = Button(self, text='Back', image=self.img3)
        self.play  = Button(self, text='Play', image=self.img4)
        self.go    = Button(self, text='Go', image=self.img5)
        self.end   = Button(self, text='End', image=self.img6)
        """
        #self.text  = Entry(self, border=3, relief=GROOVE)

        self.box.pack(side='top', expand=True, fill=BOTH) 
        #self.text.pack(fill=X)
        """
        self.start.pack(side='left', expand=True, fill=BOTH) 
        self.back.pack(side='left', expand=True, fill=BOTH) 
        self.play.pack(side='left', expand=True, fill=BOTH) 
        self.go.pack(side='left', expand=True, fill=BOTH) 
        self.end.pack(side='left', expand=True, fill=BOTH) 
        """
    def note(self, m, n):
        self.box.insert(END, '%s-%s' % (m, n))

    def reset(self):
        self.box.delete(0, END)
        
