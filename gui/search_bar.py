import tkinter as tk

class SearchBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        search_lbl = tk.Label(self, text='Search')
        search_entry = tk.Entry(self)
        search_lbl.grid(row=0, column=0)
        search_entry.grid(row=0, column=1, sticky='w')

    def search_word(self, term):
        pass