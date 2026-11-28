import tkinter as tk

class Filter(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.filters = ["Alphabet", "Type", "Title", "Date"]

        # create optionmenu
        self.var = tk.StringVar(value = self.filters[0])

        filter_option = tk.OptionMenu(self, self.var, *self.filters)
        filter_option.config(width=8)

        filter_option.grid(row=0, column=0, sticky="nsew")