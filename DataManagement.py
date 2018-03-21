import tkinter as tk
from Helper import *
import SizeInput
import networkx as nx
import matplotlib.pyplot as plt


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
        self.label_array = {}
        # Adjacency List can have 1 less edges than vertexes in graph
        if self.option == ADJACENCY_LIST_OPTION:
            self.columns -= 1
        self.matrix_int = [[int for _ in range(self.columns)] for _ in range(self.rows)]
        self.matrix_sv = [[tk.StringVar() for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_widgets()

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def init_label(self):
        tk.Label(self.root, justify="center", text=self.text_label[self.option], font=self.h.LARGE_FONT) \
            .grid(row=0, column=0, columnspan=20)

    def init_buttons(self):
        tk.Button(self.root, text="draw graph", command=self.draw_graph).grid(row=self.rows + 9, columnspan=self.rows)
        tk.Button(self.root, text="previous page",
                  command=lambda: self.h.jump_to_page(SizeInput.SizeInput, option=self.option)) \
            .grid(row=self.rows + 10, columnspan=self.rows)

    def init_entries(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if row == 0 and self.option != ADJACENCY_LIST_OPTION:
                    tk.Label(self.root, text=column + 1).grid(row=1, column=column + 1)
                if column == 0:
                    label = tk.Label(self.root, text=row + 1)
                    label.grid(row=row + 2, column=0)
                    if self.option == ADJACENCY_LIST_OPTION:
                        self.label_array[label["text"]] = row

                tk.Entry(self.root, width=2, textvariable=self.matrix_sv[row][column]) \
                    .grid(row=row + 2, column=column + 1, pady=1, padx=1)
                if self.option != ADJACENCY_LIST_OPTION:
                    self.matrix_sv[row][column].set("0")

    def draw_graph(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if tk.StringVar.get(self.matrix_sv[row][column]) == "":
                    continue
                self.matrix_int[row][column] = int(tk.StringVar.get(self.matrix_sv[row][column]))

        print(self.matrix_int)

        graph = nx.Graph()
        for vertex in range(self.rows):
            graph.add_node(vertex+1)

        if self.option == ADJACENCY_MATRIX_OPTION:
            for row in range(1, self.rows):
                for column in range(self.columns):
                    if self.matrix_int[row][column] > 0:
                        graph.add_edge(row+1, column+1)

        if self.option == ADJACENCY_LIST_OPTION:
            for row in range(self.rows):
                for column in range(self.columns):
                    pass

        plt.subplot(121)
        nx.draw(graph, with_labels=True, font_weight="bold")
        plt.show()
