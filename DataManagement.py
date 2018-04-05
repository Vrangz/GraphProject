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
                           INCIDENCE_MATRIX_OPTION: "Incidence Matrix Data Input",
                           FORM_OPTION: "Form"}
        self.matrix_int = kwargs["matrix"]
        self.matrix_sv = [[tk.StringVar() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_widgets()
        self.graph = nx.Graph()
        self.left = tk.StringVar()
        self.right = tk.StringVar()

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def init_label(self):
        tk.Label(self.root, justify="center", text=self.text_label[self.option], font=self.h.LARGE_FONT) \
            .grid(row=0, column=0, columnspan=20)
        if self.option == FORM_OPTION:
            tk.Label(self.root, justify="center", text="from", font=self.h.TEXT_FONT).grid(row=self.rows-1, column=1)
            tk.Label(self.root, justify="center", text="to", font=self.h.TEXT_FONT).grid(row=self.rows-1, column=4)

    def init_buttons(self):
        tk.Button(self.root, text="draw graph", command=self.draw_graph)\
            .grid(row=self.rows + 9, columnspan=self.rows)

        if self.option == ADJACENCY_LIST_OPTION or self.option == INCIDENCE_MATRIX_OPTION:
            tk.Button(self.root, text="convert to adjacency matrix",
                      command=self.convert_to_adjacency_matrix) \
                .grid(row=self.rows + 10, columnspan=self.rows)

        if self.option == FORM_OPTION:
            tk.Button(self.root, text="add edge", command=self.add_edge) \
                .grid(row=self.rows + 6, columnspan=self.rows)

        tk.Button(self.root, text="previous page",
                  command=lambda: self.h.jump_to_page(SizeInput.SizeInput, option=self.option)) \
            .grid(row=self.rows + 15, columnspan=self.rows)

    def init_entries(self):
        if self.option != FORM_OPTION:
            for row in range(self.rows):
                for column in range(self.columns):
                    if row == 0 and self.option != ADJACENCY_LIST_OPTION:
                        tk.Label(self.root, text=column+1).grid(row=1, column=column + 1)
                    if column == 0:
                        label = tk.Label(self.root, text=row+1)
                        label.grid(row=row + 2, column=0)

                    entry = self.draw_entry(row, column, "normal")
                    if self.option == ADJACENCY_MATRIX_OPTION:
                        if self.matrix_int[row][column] != int:
                            entry.insert(0, str(self.matrix_int[row][column]))
                    entry.grid(row=row + 2, column=column + 1, pady=1, padx=1)
        else:
            tk.Entry(self.root, width=2, justify="center", textvariable=self.matrix_sv[0][0]).grid(row=self.rows, column=1)
            tk.Entry(self.root, width=2, justify="center", textvariable=self.matrix_sv[0][1]).grid(row=self.rows, column=4)

    def convert_to_adjacency_matrix(self):
        if self.option == ADJACENCY_LIST_OPTION:
            self.set_edges(self.rows, self.columns, self.matrix_int)
            matrix_input = np.array(nx.adjacency_matrix(self.graph))
            matrix_output = [[int for _ in range(matrix_input.shape[1])] for _ in range(matrix_input.shape[0])]
            for row in range(matrix_input.shape[0]):
                for column in range(matrix_input.shape[1]):
                    matrix_output[row][column] = int((str(matrix_input[row][column]).replace(".0", "")))
            self.h.jump_to_page(DataManagement, rows=matrix_input.shape[0], columns=matrix_input.shape[1],
                                option=ADJACENCY_MATRIX_OPTION, matrix=matrix_output)

        if self.option == INCIDENCE_MATRIX_OPTION:
            matrix = self.incidence_matrix_to_adjacency(self.matrix_int)
            self.h.jump_to_page(DataManagement, rows=matrix.shape[0], columns=matrix.shape[1],
                                option=ADJACENCY_MATRIX_OPTION, matrix=matrix)

    def add_edge(self):
        self.graph.add_edge(int(tk.StringVar.get(self.matrix_sv[0][0])), int(tk.StringVar.get(self.matrix_sv[0][1])))

    def draw_graph(self):
        self.string_var_to_int_array()

        # set nodes
        for vertex in range(self.rows):
            self.graph.add_node(vertex+1)

        # set edges
        if self.option == ADJACENCY_MATRIX_OPTION:
            self.set_edges(self.rows, self.columns, self.matrix_int)
        if self.option == ADJACENCY_LIST_OPTION:
            self.set_edges(self.rows, self.columns, self.matrix_int)
        if self.option == INCIDENCE_MATRIX_OPTION:
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
