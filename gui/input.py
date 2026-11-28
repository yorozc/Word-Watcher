import tkinter as tk
from tkinter import ttk

class Input(ttk.Frame):
    def __init__(self, parent, on_submit: function):
        super().__init__(parent)
        self.on_submit = on_submit


    def handle_data(self):
        pass
