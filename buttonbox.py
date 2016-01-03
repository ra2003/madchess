from Tkinter import *

class ToolBar(Frame):
    def __init__(self, root, items, **args):
        Frame.__init__(self, master=root, **args)

        for item in items:
            btn=Button(master = self, **item)
            btn.pack(side = 'left', fill=BOTH, padx=5, pady=5)


