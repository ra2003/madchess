from Tkinter import *

class GChat(Toplevel):
    def __init__(self, root, call, nick):
        Toplevel.__init__(self, master=root)
        self.title('Chat')

        self.call = call
        self.nick = nick

        self.main = Frame(master=self,
                          border=3,
                          relief=RAISED,
                          padx=5,
                          pady=5)

        self.down = Frame(master=self,
                          border=3,
                          relief=RAISED,
                          padx=5,
                          pady=5)


        self.scrollbar = Scrollbar(master=self.main)

        self.text = Text(self.main, yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.text.yview)

        self.entry = Entry(self.down)

        self.main.pack(side='top', expand=True, fill=BOTH)
        self.down.pack(side='top', fill=X)

        self.text.pack(side='left', expand=True, fill=BOTH)
        self.scrollbar.pack(side='right', fill=Y)
        self.entry.pack(fill=X)


        self.entry.bind('<KeyPress-Return>', self.entryEnter)

    def entryEnter(self, widget):
        data = self.entry.get()
        self.text.insert(END, '<%s> %s\n' % (self.nick, data))
        self.text.yview(MOVETO, 1.0)
        self.entry.delete(0, END)
        self.call(data)

    def update(self, data):
        self.text.insert(END, '%s' % data)
        self.text.yview(MOVETO, 1.0)

if __name__ == '__main__':
    root = Tk()
    app = GChat(root, call=lambda x: x, nick='hi')
    root.mainloop()
