import tkinter as tk 
from gui.display import Display
from gui.input import Input
from gui.search_bar import SearchBar
from gui.filter import Filter

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("900x500")
        self.resizable(False, False)
        self.title("Word-Watcher")

        # configure rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # WIDGET INSTANCES
        self.search_bar = SearchBar(self)
        self.filter = Filter(self)
        self.display = Display(self)
        self.input = Input(self, on_submit=self.receive_input)

        # PLACING FRAMES ON ROOT
        # search bar & filter dropdown next to each other
        self.search_bar.grid(row=1, column=1, sticky='ew')
        self.filter.grid(row=1, column=2, sticky="w")

    def receive_input(self):
        pass
