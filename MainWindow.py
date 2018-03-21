import tkinter as tk
from OptionsPage import OptionsPage
from Helper import Helper


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.h = Helper(self.root)
        self.initialize_widgets()

    def initialize_widgets(self):
        tk.Label(self.root, text="Welcome", font=self.h.LARGE_FONT).pack(pady=10, padx=10)
        tk.Label(self.root, text="Program allows creating graphs\n press button below to continue",
                 font=self.h.TEXT_FONT).pack(pady=30, padx=10)

        tk.Button(self.root, text="Continue", command=lambda: self.h.jump_to_page(OptionsPage))\
            .pack(side="bottom", pady=30)

