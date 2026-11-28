import tkinter as tk 
from gui.display import Display
from gui.input import Input
from gui.search_bar import SearchBar

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("900x500")
        self.resizable(False, False)
        self.title("Word-Watcher")

        # configure rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        # WIDGET INSTANCES
        self.search_bar = SearchBar(self)
        self.display = Display(self)
        self.input = Input(self)

        # PLACING FRAMES ON ROOT
        self.search_bar.grid(row=1, column=1, sticky='nsew')