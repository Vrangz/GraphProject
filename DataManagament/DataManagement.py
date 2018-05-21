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
                           INCIDENCE_MATRIX_OPTION: "Incidence Matrix Data Input",
                           FORM_OPTION: "Form"}
        self.matrix_int = kwargs["matrix"]
        self.matrix_sv = [[tk.StringVar() for _ in range(self.columns)] for _ in range(self.rows)]
        self.graph = nx.Graph()
        self.color_map = ["red"]

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def init_label(self):
        tk.Label(self.root, justify="center", text=self.text_label[self.option], font=self.h.LARGE_FONT) \
            .grid(row=0, column=0, columnspan=20)

    def init_buttons(self):
        tk.Button(self.root, text="draw graph", command=self.draw_graph)\
            .grid(row=self.rows + 9, columnspan=self.rows)

        tk.Button(self.root, text="previous page",
                  command=lambda: self.h.jump_to_page(SizeInput.SizeInput, option=self.option)) \
            .grid(row=self.rows + 20, columnspan=self.rows)

    def init_entries(self):
        pass

    def convert_to_adjacency_matrix(self):
        pass

    def draw_graph(self):
        pass

    def add_vertexes(self):
        self.string_var_to_int_array()
        for vertex in range(self.rows):
            self.graph.add_node(vertex+1)

    def set_edges(self, rows, columns, array):
        pass

    def string_var_to_int_array(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if tk.StringVar.get(self.matrix_sv[row][column]) == "":
                    self.matrix_int[row][column] = 0
                else:
                    self.matrix_int[row][column] = int(tk.StringVar.get(self.matrix_sv[row][column]))

    def draw_entry(self, row, column):
        return tk.Entry(self.root, width=2, justify="center", textvariable=self.matrix_sv[row][column])

    def draw_plot(self):
        plt.subplot(111)
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos=pos, with_labels=True, font_weight="bold", node_color=self.color_map)
        plt.show()
