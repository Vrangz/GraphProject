import tkinter as tk
from Helper import Helper
import OptionsPage
from DataInput import DataInput


class SizeInput:
    def __init__(self, root, **kwargs):
        self.root = root
        self.option = kwargs["option"]
        self.h = Helper(self.root)
        self.rows = tk.StringVar()
        self.columns = tk.StringVar()
        self.int_rows = 0
        self.int_columns = 0
        self.initialize_widgets()

    def initialize_widgets(self):
        tk.Label(self.root, justify="center", text="Define number of vortexes [2-10]", font=self.h.TEXT_FONT) \
            .pack(side="top", pady="10")

        tk.Entry(self.root, textvariable=self.rows).pack(side="top", pady="10")

        if self.option == 2:
            tk.Label(self.root, justify="center", text="Define number of edges [2-10]", font=self.h.TEXT_FONT) \
                .pack(side="top", pady="10")
            tk.Entry(self.root, textvariable=self.columns).pack(side="top", pady="10")

        tk.Button(self.root, text="Continue", command=lambda: self.jump_if_correct(DataInput)) \
            .pack(side="top", pady="50")

        tk.Button(self.root, text="previous page", command=lambda: self.h.jump_to_page(OptionsPage.OptionsPage)) \
            .pack(side="bottom", pady="10")

    def jump_if_correct(self, page):
        self.int_rows = int(tk.StringVar.get(self.rows))
        if self.option == 2:
            self.int_columns = int(tk.StringVar.get(self.columns))
        else:
            self.int_columns = self.int_rows
        if self.int_rows and self.int_columns in range(2, 11):
            self.h.jump_to_page(page, rows=self.int_rows, columns=self.int_columns, option=self.option)
