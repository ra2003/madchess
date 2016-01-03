from Tkinter import *

class GMod(Frame):
    def __init__(self, mainRoot, mode=None, **args):
        Frame.__init__(self, **args)
        self.mainRoot = mainRoot
        self.instance = None

    def load(self, mode, *args, **kwargs):
        self.unload()
        self.instance = mode(self, *args, **kwargs)

        def callback(mainRoot = self.mainRoot, finish=self.instance.finish):
            finish()
            mainRoot.destroy()

        self.mainRoot.protocol('WM_DELETE_WINDOW', callback)

    def unload(self):
        if not self.instance:
            return

        for child in self.children.values():
            child.destroy()
        
        self.instance.finish()
        
        self.instance = None

