import tkinter as tk
from DataManagament.DataManagement import DataManagement


class AdjacencyMatrix(DataManagement):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.initialize_widgets()

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def draw_graph(self):
        self.graph.clear()
        self.add_vertexes()
        self.set_edges(self.rows, self.columns, self.matrix_int)
        self.draw_plot()

    def set_edges(self, rows, columns, array):
        for row in range(rows):
            for column in range(columns):
                if array[row][column] > 0:
                    self.graph.add_edge(row + 1, column + 1)

    def init_entries(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0:
                    tk.Label(self.root, text=column+1).grid(row=1, column=column + 1)
                if column == 0:
                    label = tk.Label(self.root, text=row+1)
                    label.grid(row=row + 2, column=0)

                entry = self.draw_entry(row, column)
                if self.matrix_int[row][column] != int:
                    entry.insert(0, str(self.matrix_int[row][column]))
                entry.grid(row=row + 2, column=column + 1, pady=1, padx=1)
