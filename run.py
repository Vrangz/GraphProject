import tkinter as tk
from MainWindow import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    tk.Tk.wm_title(root, "Grafy i sieci w informatyce")
    tk.Tk.resizable(root, 0, 0)
    MainWindow(root)
    root.mainloop()
