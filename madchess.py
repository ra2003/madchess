from Tkinter import *
from mod.local.glocal import *
from mod.host.ghost import *
from gclock import *
from gmod import *
from gboard import *
from statusbar import *
from gmove import *
from buttonbox import *

class AppChess(object):
    def __init__(self, root):
        self.root = root
        self.root.title('madchess')



        self.main = Frame(master=self.root, padx=10, pady=10)


        self.down = Frame(master=self.main) 
        self.left = Frame(master=self.down,
                          padx=5,
                          pady=5,
                          border=3,
                          relief=RAISED)

        self.right = Frame(master=self.down)        

        self.status = Statusbar(self.root)


        self.initializeToolbar()

        self.initializeGBoard()
        self.initializeMenubar()
        self.initializeFileMenu()
        self.initializePlayMenu()
        self.initializeBoardMenu()
        self.initializeHelpMenu()

    
        self.root.config(menu=self.menubar)
       

        self.main.pack(side = 'top',
                            fill = BOTH,
                            expand = True)

        self.down.pack(side = 'left',
                             fill = BOTH,
                             expand = True)

        self.left.pack(side = 'left',
                             fill = BOTH,
                             expand = True)

        self.right.pack(side = 'left',
                             fill = BOTH,
                             expand = True)



        self.initializeGMod()
        self.initializeGClock()
        self.initializeGMove()
        self.gmod.load(GLocal, self.gboard, self.gclock, self.gmove)

        self.gboard.setNote(self.gmove.note)

        self.gboard.bind('<<VALID-MOVE>>', lambda x: self.gclock.invert())

        self.gboard.bind('<<CHECK-MATE>>', 
                            lambda x:
                                (self.gclock.stop(), self.status.set('Check mate !!!')))

        self.gboard.bind('<<DRAW>>', 
                            lambda x:
                                (self.gclock.stop(), self.status.set('Draw !!!')))

       
        self.gboard.bind('<<INVALID-MOVE>>', lambda x: self.status.set('Invalid move !!!'))

        self.gclock.bind('<<zero>>', 
                         lambda x: self.status.set('Time is over !!!'))


        self.status.pack(side=BOTTOM, fill=X)

    def initializeGBoard(self):
        self.gboard = GBoard(self.left, 
                             None, 
                             self.status)


        self.gboard.pack(expand=True)

    def initializeGMod(self):
        self.gmod = GMod(mainRoot=self.root,
                         master=self.right, 
                         padx=5, 
                         pady=5, 
                         border=3, 
                         relief=RAISED)


        self.gmod.pack(side = 'top',
                             fill = BOTH)



    def initializeGMove(self):
        self.gmove = GMove(self.right, 
                           relief=RAISED,
                           padx=5, 
                           pady=5,
                           border=3)

        self.gmove.pack(side = 'top',
                             expand=True, 
                             fill = BOTH)


    def initializeGClock(self):
        self.gclock = GClock(self.right,
                             relief = RAISED,
                             padx=5,
                             pady=5,
                             border=3)

        self.gclock.pack(side='top', fill=X)

    def initializeMenubar(self):
        self.menubar = Menu(master=self.root)

    def initializeFileMenu(self):
        self.filemenu = Menu(self.menubar, tearoff = 0) 
   
        self.filemenu.add_command(label='Export', command = self.save)

        self.filemenu.add_separator()
        self.filemenu.add_command(label='Quit', command = self.root.quit)

        self.menubar.add_cascade(label='File', menu=self.filemenu)
    
    def initializePlayMenu(self):
        self.playmenu = Menu(self.menubar, tearoff = 0)

        self.playmenu.add_command(label='Direct', 
                                  command = lambda: 
                                  self.gmod.load(GHost, self.gboard, self.gclock, self.gmove))
        
        self.playmenu.add_command(label='Human', 
                                  command = lambda: 
                                  self.gmod.load(GLocal, self.gboard, self.gclock, self.gmove))

 
        self.menubar.add_cascade(label='Play', menu=self.playmenu)



    def initializeBoardMenu(self):
        self.boardmenu = Menu(self.menubar, tearoff = 0)
        
        self.boardmenu.add_command(label='Zoom in board', 
                                   command = lambda rate=3: self.gboard.zoomInBoard(rate))

        self.boardmenu.add_command(label='Zoom out board',
                                   command = lambda rate=3: self.gboard.zoomOutBoard(rate))


        self.menubar.add_cascade(label='Board', menu=self.boardmenu)


    def initializeHelpMenu(self):
        self.helpmenu = Menu(self.menubar, tearoff = 0)

        self.helpmenu.add_command(label='About', command = self.about)
        self.menubar.add_cascade(label='help', menu=self.helpmenu)


    def initializeToolbar(self):
        self.img1 = PhotoImage(file='icon/EnvelopeOpen.gif')

        self.img2 = PhotoImage(file='icon/MagnifyPlus.gif')
        self.img3 = PhotoImage(file='icon/MagnifyMinus.gif')

        self.img4 = PhotoImage(file='icon/Invert.gif')
        self.img5 = PhotoImage(file='icon/Computer.gif')
        self.img6 = PhotoImage(file='icon/World.gif')
        self.img7 = PhotoImage(file='icon/Users.gif')
        self.img8 = PhotoImage(file='icon/Home.gif')

        self.toolbar = ToolBar(self.main, 
                               (
                                  {
                                       'text':'Export',
                                       'image':self.img1
                                   },


                                   {
                                       'text':'Plus',
                                       'image':self.img2,
                                       'command':lambda rate=3: self.gboard.zoomInBoard(rate)
                                   },
                                   {
                                       'text':'Minus',
                                       'image':self.img3,
                                       'command':lambda rate=3: self.gboard.zoomOutBoard(rate)
                                   },
                                   {
                                       'text':'Invert',
                                       'image':self.img4,
                                   },
                                   {
                                       'text':'Direct',
                                       'command':lambda: 
                                            self.gmod.load(GHost, self.gboard, 
                                                self.gclock, self.gmove),                                                              'image':self.img7
                                   },
                                   {
                                       'text':'Local',
                                       'image':self.img8,
                                       'command': lambda:
                                             self.gmod.load(GLocal, self.gboard, 
                                                 self.gclock, self.gmove)         
                                   }
                                   

                               ), 
                               
                               border=3, 
                               relief=RAISED)

        self.toolbar.pack(side='top', fill=X)

    def save(self):
        pass

    def about(self):
        pass


if __name__ == "__main__":
    root =  Tk()

    app = AppChess(root)

    root.mainloop()
