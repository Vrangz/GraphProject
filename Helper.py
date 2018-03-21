ADJACENCY_MATRIX_OPTION = 0
ADJACENCY_LIST_OPTION = 1
INCIDENCE_MATRIX_OPTION = 2


class Helper:
    LARGE_FONT = ("Verdana", 18)
    TEXT_FONT = ("Verdana", 12)

    def __init__(self, root):
        self.root = root

    def jump_to_page(self, page, **kwargs):
        for widget in self.root.winfo_children():
            widget.destroy()
        page(self.root, **kwargs)
