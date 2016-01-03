from Tkinter import *
from tkMessageBox import showwarning

class GAsk(Toplevel):
    def __init__(self, root):
        self.root = root

        Toplevel.__init__(self, master=root, padx=10, pady=10)

        self.title('Host ip')

        self.resizable(height=False, width=False)

        self.frame1 = Frame(master=self,
                           padx=5,
                           pady=5,
                           border=3,
                           relief=RAISED)


        self.l1 = Label(master=self.frame1, text="Ip:")
        self.l1.grid(row=0, column=0, sticky=E)

        self.e1 = Entry(master=self.frame1)
        self.e1.grid(row=0, column=1)


 
        self.l2 = Label(master=self.frame1, text="Port:")
        self.l2.grid(row=1, column=0, sticky=E)

        self.e2 = Entry(master=self.frame1)

        self.e2.grid(row=1, column=1)

        self.frame1.pack(side='top', fill=BOTH)

        self.l3 = Label(master=self.frame1, text="Nick:")
        self.l3.grid(row=2, column=0, sticky=E)

        self.e3 = Entry(master=self.frame1)
        self.e3.grid(row=2, column=1, sticky=E)

        self.frame2 = Frame(master=self,
                           padx=5,
                           pady=5,
                           border=3,
                           relief=RAISED)


        self.frame2.pack(side='top', fill=X)

        self.b1 = Button(master=self.frame2, text='Ok', command=self.ok)
        self.b2 = Button(master=self.frame2, text='Cancel', command=self.cancel)

        self.b1.pack(side='left', expand=True, fill=X)
        self.b2.pack(side='left', expand=True, fill=X)

        self.info = None

        self.master.wait_window(self)

    def cancel(self):
        self.destroy()

    def ok(self):
        opt1 = self.e1.get()
        opt2 = self.e2.get()
        opt3 = self.e3.get()

        try:
            opt2 = int(opt2)
        except:
            showwarning('Host', 'Please, the port number must be an integer !!')
            return

        if not (opt1 and opt2 and opt3):
            showwarning('Host', 'You must fill both fields !')
            return

        self.info = (opt1, opt2, opt3)
        self.destroy()

    def get(self):
        return self.info

if __name__ == '__main__':
    root = Tk()
    app = GAsk(root)
    root.mainloop()
