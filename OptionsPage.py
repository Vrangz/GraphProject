import tkinter as tk
import MainWindow
from Helper import Helper
from SizeInput import SizeInput


class OptionsPage:
    def __init__(self, root):
        self.root = root
        self.h = Helper(self.root)
        self.initialize_widgets()

    def initialize_widgets(self):
        tk.Label(self.root, justify="center", text="Choose your graph data input representation",
                 font=self.h.LARGE_FONT).grid(row=0, column=0, columnspan=25, sticky="n")

        tk.Label(self.root, text="Adjacency matrix is a square matrix, vertexes are\n"
                                 "represented by rows and columns in matrix.\n"
                                 "Positive value represents an edge between two vertexes.\n"
                                 "Matrix should be symmetrical at the diagonal\n"
                                 "when vertexes do not contain loops to themselves\n",
                 font=self.h.TEXT_FONT).grid(row=1, column=0, sticky="w")

        tk.Button(self.root, text="adjacency matrix",
                  command=self.adjacency_matrix_data_input).grid(row=7, column=0, columnspan=2)

        tk.Label(self.root, text="Adjacency list is a list which specify\n"
                                 "edges for every vertex. Every row of a list\n"
                                 "starts with number of vertex and after are\n"
                                 "specified vertexes that connects to this one\n",
                 font=self.h.TEXT_FONT).grid(row=1, column=5, sticky="w")

        tk.Button(self.root, text="adjacency list",
                  command=self.adjacency_list_data_input).grid(row=7, column=5, columnspan=2)

        tk.Label(self.root, text="Incidence matrix is a rectangular matrix,\n"
                                 "it represents relations between vertexes\n"
                                 "by rows and edges by columns. \n"
                                 "Positive value represents existence of\n"
                                 "the connection between two vertexes\n",
                 font=self.h.TEXT_FONT).grid(row=1, column=10, sticky="w")

        tk.Button(self.root, text="incidence matrix",
                  command=self.incidence_matrix_data_input).grid(row=7, column=10, columnspan=2)

        tk.Label(self.root, text="Create a graph using form.\n"
                                 "Define number of vertexes and then\n"
                                 "join edges as you like\n",
                 font=self.h.TEXT_FONT).grid(row=1, column=15, sticky="w")

        tk.Button(self.root, text="form",
                  command=self.form_input).grid(row=7, column=15, columnspan=2)

        tk.Button(self.root, text="previous page", command=lambda: self.h.jump_to_page(MainWindow.MainWindow)) \
            .grid(row=8, column=6, sticky="s", columnspan=2)

    def adjacency_matrix_data_input(self):
        self.h.jump_to_page(SizeInput, option=0)

    def adjacency_list_data_input(self):
        self.h.jump_to_page(SizeInput, option=1)

    def incidence_matrix_data_input(self):
        self.h.jump_to_page(SizeInput, option=2)

    def form_input(self):
        self.h.jump_to_page(SizeInput, option=3)
