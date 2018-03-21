import tkinter as tk
from Helper import Helper
import SizeInput


class DataInput:
    def __init__(self, root, **kwargs):
        self.root = root
        self.rows = kwargs["rows"]
        self.columns = kwargs["columns"]
        self.option = kwargs["option"]
        self.text_label = {0: "Adjacency Matrix Data Input",
                           1: "Adjacency List Data Input",
                           2: "Incidence Matrix Data Input"}
        self.h = Helper(self.root)
        # Adjacency List can have 1 less edges than vertexes in graph
        if self.option == 1:
            self.columns -= 1
        self.matrix_int = [[int for _ in range(self.columns)] for _ in range(self.rows)]
        self.matrix_sv = [[tk.StringVar() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_widgets()

    def initialize_widgets(self):
        # Label
        tk.Label(self.root, justify="center", text=self.text_label[self.option], font=self.h.LARGE_FONT) \
            .grid(row=0, column=0, columnspan=20)

        # Drawing Input Fields
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0:
                    tk.Label(self.root, text=column + 1).grid(row=1, column=column + 1)
                if column == 0:
                    tk.Label(self.root, text=row + 1).grid(row=row + 2, column=0)

                tk.Entry(self.root, width=2, textvariable=self.matrix_sv[row][column]) \
                    .grid(row=row + 2, column=column + 1, pady=1, padx=1)
                if self.option != 1:
                    self.matrix_sv[row][column].set("0")

        # Buttons
        tk.Button(self.root, text="draw graph", command=self.draw_graph).grid(row=self.rows + 9, columnspan=self.rows)
        tk.Button(self.root, text="previous page",
                  command=lambda: self.h.jump_to_page(SizeInput.SizeInput, option=self.option)) \
            .grid(row=self.rows + 10, columnspan=self.rows)

    def draw_graph(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.matrix_int[row][column] = int(tk.StringVar.get(self.matrix_sv[row][column]))
        print(self.matrix_int)
