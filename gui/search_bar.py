import tkinter as tk

class SearchBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        search_entry = tk.Entry(self)
        search_btn = tk.Button(self, text='Search')
        search_entry.grid(row=0, column=0, sticky='nsew')
        search_btn.grid(row=0, column=1)

    def search_word(self, term):
        pass