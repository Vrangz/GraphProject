import tkinter as tk
from Helper import *
import SizeInput
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class DataManagement:
    def __init__(self, root, **kwargs):
        self.root = root
        self.rows = kwargs["rows"]
        self.columns = kwargs["columns"]
        self.option = kwargs["option"]
        self.h = Helper(self.root)
        self.text_label = {ADJACENCY_MATRIX_OPTION: "Adjacency Matrix Data Input",
                           ADJACENCY_LIST_OPTION: "Adjacency List Data Input",
                           INCIDENCE_MATRIX_OPTION: "Incidence Matrix Data Input"}
        # Adjacency List can have 1 less edges than vertexes in graph
        if self.option == ADJACENCY_LIST_OPTION:
            self.columns -= 1
        self.matrix_int = [[int for _ in range(self.columns)] for _ in range(self.rows)]
        self.matrix_sv = [[tk.StringVar() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_widgets()
        self.graph = nx.Graph()
        print(self.rows, self.columns, self.option)

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def init_label(self):
        tk.Label(self.root, justify="center", text=self.text_label[self.option], font=self.h.LARGE_FONT) \
            .grid(row=0, column=0, columnspan=20)

    def init_buttons(self):
        tk.Button(self.root, text="draw graph", command=self.draw_graph)\
            .grid(row=self.rows + 9, columnspan=self.columns)

        if self.option != ADJACENCY_MATRIX_OPTION:
            tk.Button(self.root, text="convert to adjacency matrix",
                      command=self.convert_to_adjacency_matrix) \
                .grid(row=self.rows + 10, columnspan=self.columns)

        tk.Button(self.root, text="previous page",
                  command=lambda: self.h.jump_to_page(SizeInput.SizeInput, option=self.option)) \
            .grid(row=self.rows + 15, columnspan=self.columns)

    def convert_to_adjacency_matrix(self):
        if self.option == ADJACENCY_LIST_OPTION:
            self.set_edges(self.rows, self.columns, self.matrix_int)
            matrix = nx.adjacency_matrix(self.graph)
            print(matrix)

        if self.option == INCIDENCE_MATRIX_OPTION:
            matrix = self.incidence_matrix_to_adjacency(self.matrix_int)
            print(matrix)

    def init_entries(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0 and self.option != ADJACENCY_LIST_OPTION:
                    tk.Label(self.root, text=column+1).grid(row=1, column=column + 1)
                if column == 0:
                    label = tk.Label(self.root, text=row+1)
                    label.grid(row=row + 2, column=0)

                entry = self.draw_entry(row, column, "normal")
                entry.grid(row=row + 2, column=column + 1, pady=1, padx=1)

    def draw_graph(self):
        self.string_var_to_int_array()
        # set nodes
        for vertex in range(self.rows):
            self.graph.add_node(vertex+1)

        # set edges
        if self.option == (ADJACENCY_MATRIX_OPTION or ADJACENCY_LIST_OPTION):
            self.set_edges(self.rows, self.columns, self.matrix_int)
        else:
            matrix = self.incidence_matrix_to_adjacency(self.matrix_int)
            self.set_edges(matrix.shape[0], matrix.shape[1], matrix)

        self.draw_plot()

    def set_edges(self, rows, columns, array):
        for row in range(rows):
            for column in range(columns):
                if array[row][column] > 0:
                    if self.option == ADJACENCY_LIST_OPTION:
                        self.graph.add_edge(row+1, array[row][column])
                        continue
                    self.graph.add_edge(row + 1, column + 1)

    def string_var_to_int_array(self):
        # StringVar matrix to int matrix
        for row in range(self.rows):
            for column in range(self.columns):
                if tk.StringVar.get(self.matrix_sv[row][column]) == "":
                    self.matrix_int[row][column] = 0
                else:
                    self.matrix_int[row][column] = int(tk.StringVar.get(self.matrix_sv[row][column]))

    def incidence_matrix_to_adjacency(self, array):
        incidence_matrix = np.array(array)
        adjacency_matrix = (np.dot(incidence_matrix, incidence_matrix.T) > 0).astype(int)
        nx.from_numpy_matrix(adjacency_matrix)
        np.fill_diagonal(adjacency_matrix, 0)
        return adjacency_matrix

    def draw_entry(self, row, column, state):
        return tk.Entry(self.root, width=2, justify="center", state=state, textvariable=self.matrix_sv[row][column])

    def draw_plot(self):
        plt.subplot(111)
        nx.draw(self.graph, with_labels=True, font_weight="bold")
        plt.show()
