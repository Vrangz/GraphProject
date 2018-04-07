import tkinter as tk
from DataManagament.DataManagement import DataManagement


class Form(DataManagement):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.initialize_widgets()
        self.left = tk.StringVar()
        self.right = tk.StringVar()

    def init_label(self):
        super().init_label()
        tk.Label(self.root, justify="center", text="from", font=self.h.TEXT_FONT).grid(row=self.rows - 1, column=1)
        tk.Label(self.root, justify="center", text="to", font=self.h.TEXT_FONT).grid(row=self.rows - 1, column=4)

    def init_buttons(self):
        super().init_buttons()
        tk.Button(self.root, text="add edge", command=self.add_edge).grid(row=self.rows + 6, columnspan=self.rows)
        tk.Button(self.root, text="remove edge", command=self.remove_edge).grid(row=self.rows+7, columnspan=self.rows)

    def init_entries(self):
        tk.Entry(self.root, width=2, justify="center", textvariable=self.matrix_sv[0][0]). \
            grid(row=self.rows, column=1)
        tk.Entry(self.root, width=2, justify="center", textvariable=self.matrix_sv[0][1]). \
            grid(row=self.rows, column=4)

    def draw_graph(self):
        self.add_vertexes()
        self.draw_plot()

    def add_edge(self):
        self.graph.add_edge(int(tk.StringVar.get(self.matrix_sv[0][0])), int(tk.StringVar.get(self.matrix_sv[0][1])))

    def remove_edge(self):
        self.graph.remove_edge(int(tk.StringVar.get(self.matrix_sv[0][0])), int(tk.StringVar.get(self.matrix_sv[0][1])))