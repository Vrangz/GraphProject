import tkinter as tk
from Helper import *
import OptionsPage
from DataManagament.AdjacencyList import AdjacencyList
from DataManagament.AdjacencyMatrix import AdjacencyMatrix
from DataManagament.Form import Form
from DataManagament.IncidenceMatrix import IncidenceMatrix


class SizeInput:
    def __init__(self, root, **kwargs):
        self.root = root
        self.option = kwargs["option"]
        self.h = Helper(self.root)
        self.rows = tk.StringVar()
        self.columns = tk.StringVar()
        self.rows_int = 0
        self.columns_int = 0
        self.initialize_widgets()

    def initialize_widgets(self):
        tk.Label(self.root, justify="center", text="Define number of vertexes [2-10]", font=self.h.TEXT_FONT) \
            .pack(side="top", pady="10")

        tk.Entry(self.root, textvariable=self.rows).pack(side="top", pady="10")

        if self.option == INCIDENCE_MATRIX_OPTION:
            tk.Label(self.root, justify="center", text="Define number of edges [2-14]", font=self.h.TEXT_FONT) \
                .pack(side="top", pady="10")
            tk.Entry(self.root, textvariable=self.columns).pack(side="top", pady="10")

        tk.Button(self.root, text="Continue", command=lambda: self.jump_if_correct()) \
            .pack(side="top", pady="50")

        tk.Button(self.root, text="previous page", command=lambda: self.h.jump_to_page(OptionsPage.OptionsPage)) \
            .pack(side="bottom", pady="10")

    def jump_if_correct(self):
        self.rows_int = int(tk.StringVar.get(self.rows))

        if self.option == INCIDENCE_MATRIX_OPTION:
            self.columns_int = int(tk.StringVar.get(self.columns))
        else:
            self.columns_int = self.rows_int

        if (self.rows_int and self.columns_int) in range(2, 15):
            if self.option == ADJACENCY_LIST_OPTION:
                self.columns_int -= 1
            matrix_int = [[int for _ in range(self.columns_int)] for _ in range(self.rows_int)]
            page = {ADJACENCY_MATRIX_OPTION: AdjacencyMatrix,
                    ADJACENCY_LIST_OPTION: AdjacencyList,
                    INCIDENCE_MATRIX_OPTION: IncidenceMatrix,
                    FORM_OPTION: Form}

            self.h.jump_to_page(page[self.option], rows=self.rows_int, columns=self.columns_int, option=self.option,
                                matrix=matrix_int)
