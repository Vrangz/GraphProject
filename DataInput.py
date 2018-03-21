import tkinter as tk
from Helper import Helper
import SizeInput


class DataInput:
    def __init__(self, root, **kwargs):
        self.root = root
        self.rows = kwargs["rows"]
        self.columns = kwargs["columns"]
        self.option = kwargs["option"]
        self.h = Helper(self.root)
        # array of StringVar
        self.matrix = [[tk.StringVar() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_widgets()

    def initialize_widgets(self):
        tk.Label(self.root, justify="center", text="Adjacency Matrix Data Input", font=self.h.LARGE_FONT) \
            .grid(row=0, column=0, columnspan=20)

        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0:
                    tk.Label(self.root, text=column + 1).grid(row=1, column=column+1)
                if column == 0:
                    tk.Label(self.root, text=row + 1).grid(row=row+2, column=0)

                tk.Entry(self.root, width=2, textvariable=self.matrix[row][column]) \
                    .grid(row=row + 2, column=column + 1, pady=1, padx=1)
                self.matrix[row][column].set("0")

        tk.Button(self.root, text="draw graph", command=self.draw_graph).grid(row=self.rows + 9, columnspan=self.rows)
        tk.Button(self.root, text="previous page",
                  command=lambda: self.h.jump_to_page(SizeInput.SizeInput, option=self.option))\
            .grid(row=self.rows + 10, columnspan=self.rows)
        print(self.rows, self.columns, self.option)

    def draw_graph(self):
        mtx = [[int for _ in range(self.columns)] for _ in range(self.rows)]
        for row in range(self.rows):
            for column in range(self.columns):
                mtx[row][column] = int(tk.StringVar.get(self.matrix[row][column]))
        print(mtx)
        self.root.g