from tkinter import *
from .system_input import system_input
from .solve_button import solve_button
from .results_output import results_output
from .omega_plot_output import omega_plot_output


class View:

    def __init__(self):
        root = Tk()
        root.title("Математичне моделювання. Лабораторна робота №1")

        self.frames_columns_rows = {"system_input": [0, 0],
                                    "solve_button": [1, 0],
                                    "results_output": [2, 0],
                                    "omega_plot_output": [3, 0],
                                    }

        self.system_input = system_input(root, self.frames_columns_rows["system_input"])
        self.solve_button = solve_button(root, self.frames_columns_rows["solve_button"], self)
        self.results_output = results_output(root, self.frames_columns_rows["results_output"])
        self.omega_plot_output = omega_plot_output(root, self.frames_columns_rows["omega_plot_output"])

        root.mainloop()
