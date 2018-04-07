import tkinter as tk
from Helper import *
import networkx as nx
import numpy as np
from DataManagament.AdjacencyMatrix import AdjacencyMatrix
from DataManagament.DataManagement import DataManagement


class AdjacencyList(DataManagement):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.initialize_widgets()

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def init_buttons(self):
        super().init_buttons()
        tk.Button(self.root, text="convert to adjacency matrix", command=self.convert_to_adjacency_matrix) \
            .grid(row=self.rows + 10, columnspan=self.rows)

    def init_entries(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if column == 0:
                    label = tk.Label(self.root, text=row + 1)
                    label.grid(row=row + 2, column=0)

                entry = self.draw_entry(row, column)
                entry.grid(row=row + 2, column=column + 1, pady=1, padx=1)

    def convert_to_adjacency_matrix(self):
        self.set_edges(self.rows, self.columns, self.matrix_int)
        matrix_input = np.array(nx.to_numpy_matrix(self.graph))
        matrix_output = [[int for _ in range(matrix_input.shape[1])] for _ in range(matrix_input.shape[0])]

        for row in range(matrix_input.shape[0]):
            for column in range(matrix_input.shape[1]):
                matrix_output[row][column] = int(str(matrix_input[row][column]).replace(".0", ""))

        self.h.jump_to_page(AdjacencyMatrix, rows=matrix_input.shape[0], columns=matrix_input.shape[0],
                            option=ADJACENCY_MATRIX_OPTION, matrix=matrix_output)

    def draw_graph(self):
        self.graph.clear()
        self.add_vertexes()
        self.set_edges(self.rows, self.columns, self.matrix_int)
        self.draw_plot()

    def set_edges(self, rows, columns, array):
        for row in range(rows):
            for column in range(columns):
                if array[row][column] > 0:
                    self.graph.add_edge(row + 1, array[row][column])
