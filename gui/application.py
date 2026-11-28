import tkinter as tk 
from gui.display import Display
from gui.input import Input

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("900x500")
        self.resizable(False, False)
        self.title("Word-Watcher")

        # configure columns

        # WIDGET INSTANCES
        self.display = Display(self)

        self.input = Input(self)