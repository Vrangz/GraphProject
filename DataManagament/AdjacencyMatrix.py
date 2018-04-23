import tkinter as tk
import networkx as nx
from collections import deque
from itertools import chain
from DataManagament.DataManagement import DataManagement


class AdjacencyMatrix(DataManagement):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.color_option = tk.StringVar()
        self.initialize_widgets()

    def initialize_widgets(self):
        self.init_label()
        self.init_entries()
        self.init_buttons()

    def init_buttons(self):
        super().init_buttons()
        tk.Button(self.root, text="is eulerian", command=self.is_eulerian).\
            grid(row=self.rows + 10, columnspan=self.rows)
        tk.Button(self.root, text="is hamiltonian", command=self.is_hamiltonian). \
            grid(row=self.rows + 11, columnspan=self.rows)
        tk.Button(self.root, text="BFS", command=self.bfs). \
            grid(row=self.rows + 12, columnspan=self.rows)
        tk.Button(self.root, text="color graph", command=self.bfs). \
            grid(row=self.rows + 13, column=self.columns//2-1, columnspan=self.rows)
        tk.Button(self.root, text="bridges", command=self.bridges). \
            grid(row=self.rows + 14, columnspan=self.rows)

    def is_eulerian(self):
        eulerian = nx.is_eulerian(self.graph)
        print(self.graph)
        if eulerian:
            print("Graph is eulerian")
        else:
            print("Graph is not eulerian")

    def is_hamiltonian(self):
        print(self.matrix_int)
        path = [-1] * self.rows
        path[0] = 0
        if not self.ham_cycle_util(path, 1):
            return False

        self.print_solution(path)
        return True

    def ham_cycle_util(self, path, pos):
        if pos == self.rows:
            if self.matrix_int[path[pos - 1]][path[0]] >= 1:
                return True
            else:
                return False

        for v in range(1, self.rows):
            if self.is_safe(v, pos, path):
                path[pos] = v

                if self.ham_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1

        return False

    def is_safe(self, v, pos, path):
        if self.matrix_int[path[pos - 1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False
        return True

    def print_solution(self, path):
        print("Graph is hamiltonian - following is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex+1)
        print(path[0]+1, "\n")

    def bfs(self):
        G = self.graph
        root = 1
        edges = self.bfs_edges(G, root)
        nodes = [root] + [v for u, v in edges]
        print(nodes)

    def bfs_edges(self, G, source, reverse=False):
        if reverse and G.is_directed():
            successors = G.predecessors
        else:
            successors = G.neighbors
        for e in self.generic_bfs_edges(G, source, successors):
            yield e

    def generic_bfs_edges(self, G, source, neighbors=None):
        visited = {source}
        queue = deque([(source, neighbors(source))])
        while queue:
            parent, children = queue[0]
            try:
                child = next(children)
                if child not in visited:
                    yield parent, child
                    visited.add(child)
                    queue.append((child, neighbors(child)))
            except StopIteration:
                queue.popleft()

    def bridges(self):
        print(list(self.util_bridges()))

    def util_bridges(self):
        root = 1
        chains = nx.chain_decomposition(self.graph, root)
        chain_edges = set(chain.from_iterable(chains))
        for u, v in self.graph.edges():
            if (u, v) not in chain_edges and (v, u) not in chain_edges:
                yield u, v

    def color_graph(self):
        option = tk.StringVar.get(self.color_option)
        print(option)
        if option == 0:
            nx.coloring.greedy_color(self.graph)

        if option == 1:
            nx.coloring.greedy_color(self.graph, strategy="largest_first")

        if option == 2:
            nx.coloring.greedy_color(self.graph, strategy="random_sequential")

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
                    tk.Label(self.root, text=column + 1).grid(row=1, column=column + 1)
                if column == 0:
                    label = tk.Label(self.root, text=row + 1)
                    label.grid(row=row + 2, column=0)

                entry = self.draw_entry(row, column)
                if self.matrix_int[row][column] != int:
                    entry.insert(0, str(self.matrix_int[row][column]))
                entry.grid(row=row + 2, column=column + 1, pady=1, padx=1)

        tk.Entry(self.root, width=2, textvariable=self.color_option)\
            .grid(row=self.rows + 13, column=self.columns//2+1, columnspan=self.rows)
