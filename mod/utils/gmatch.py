from Tkinter import *
from tkMessageBox import showwarning

class GMatch(Toplevel):
    def __init__(self, root):
        self.root = root
        Toplevel.__init__(self, master=root, padx=10, pady=10)

        self.title('Match')

        self.resizable(height=False, width=False)

        self.frame1 = Frame(master=self,
                            padx=5,
                            pady=5,
                            border=3,
                            relief=RAISED)

        self.img1 = PhotoImage(master=self.frame1, file='img/white/pawn.gif')
        self.img2 = PhotoImage(master=self.frame1, file='img/black/pawn.gif')

        self.opt = IntVar()

        self.opt.set(12) 

        self.radiobutton1 = Radiobutton(master=self.frame1, 
                                        image=self.img1, 
                                        indicatoron=0,
                                        variable=self.opt,
                                        value=12)

        self.radiobutton2 = Radiobutton(master=self.frame1, 
                                        image=self.img2, 
                                        indicatoron=0,
                                        variable=self.opt,
                                        value=13)

        self.radiobutton1.pack(side='left', expand=True, fill=X)
        self.radiobutton2.pack(side='left', expand=True, fill=X)


        self.frame1.pack(side='top', fill=BOTH)

        self.frame2 = Frame(master=self,
                            padx=5,
                            pady=5,
                            border=3,
                            relief=RAISED)


        self.label1 = Label(master=self.frame2, text='Time:')
        self.entry1 = Entry(master=self.frame2)

        self.label2 = Label(master=self.frame2, text='Increment:')
        self.entry2 = Entry(master=self.frame2)


        self.label1.grid(row=0, column=0, sticky=E)
        self.entry1.grid(row=0, column=1, sticky=E)
        self.frame2.pack(side='top', fill=BOTH)

        self.frame3 = Frame(master=self,
                            padx=5,
                            pady=5,
                            border=3,
                            relief=RAISED)
    
        self.button1 = Button(master=self.frame3,text='Ok', command=self.ok)
        self.button2 = Button(master=self.frame3,text='Cancel', command=self.cancel)
        self.button1.pack(side='left', expand=True, fill=BOTH)
        self.button2.pack(side='left', expand=True, fill=BOTH)

        self.frame3.pack(side='top', fill=BOTH)
        """I must fix it, it isn't closing the window i have to define a protocol"""
        self.wait_window()

    def ok(self):
        try:
            time = int(self.entry1.get())
        except:
            showwarning('Warning !', 'The values must be integers !!!')
            return

        opt = self.opt

        self.info = (opt.get(), time)

        self.destroy()

    def cancel(self):
        self.info = None
        self.destroy()

if __name__ == '__main__':
    root = Tk()
    app = GMatch(root)
    root.mainloop()

    pass


