import tkinter as tk
from Helper import *
import networkx as nx
import numpy as np
from DataManagament.AdjacencyMatrix import AdjacencyMatrix
from DataManagament.DataManagement import DataManagement


class IncidenceMatrix(DataManagement):
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
                if row == 0:
                    tk.Label(self.root, text=column + 1).grid(row=1, column=column + 1)
                if column == 0:
                    label = tk.Label(self.root, text=row + 1)
                    label.grid(row=row + 2, column=0)

                entry = self.draw_entry(row, column)
                entry.grid(row=row + 2, column=column + 1, pady=1, padx=1)

    def convert_to_adjacency_matrix(self):
        matrix = self.incidence_matrix_to_adjacency(self.matrix_int)
        self.h.jump_to_page(AdjacencyMatrix, rows=matrix.shape[0], columns=matrix.shape[1],
                            option=ADJACENCY_MATRIX_OPTION, matrix=matrix)

    def draw_graph(self):
        self.graph.clear()
        self.add_vertexes()
        matrix = self.incidence_matrix_to_adjacency(self.matrix_int)
        self.set_edges(matrix.shape[0], matrix.shape[1], matrix)
        self.draw_plot()

    def set_edges(self, rows, columns, array):
        for row in range(rows):
            for column in range(columns):
                if array[row][column] > 0:
                    self.graph.add_edge(row + 1, column + 1)

    def incidence_matrix_to_adjacency(self, array):
        incidence_matrix = np.array(array)
        adjacency_matrix = (np.dot(incidence_matrix, incidence_matrix.T) > 0).astype(int)
        nx.from_numpy_matrix(adjacency_matrix)
        np.fill_diagonal(adjacency_matrix, 0)
        return adjacency_matrix
