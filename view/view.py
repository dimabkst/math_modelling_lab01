from tkinter import *
from tkinter import ttk
from .system_input import system_input
from .solve_button import solve_button
from .results_output import results_output
from .omega_plot_output import omega_plot_output


class View:

    def __init__(self):
        self.root = Tk()
        self.root.configure(bg="white")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.title("Математичне моделювання. Лабораторна робота №1")

        self.frames_columns_rows = {"system_input": [0, 0],
                                    "solve_button": [0, 1],
                                    "results_output": [0, 2],
                                    "omega_plot_output": [1, 0],
                                    }

        self.system_input = system_input(self.root, self.frames_columns_rows["system_input"])
        self.solve_button = solve_button(self.root, self.frames_columns_rows["solve_button"], self)
        self.results_output = results_output(self.root, self.frames_columns_rows["results_output"])
        self.omega_plot_output = omega_plot_output(self.root, self.frames_columns_rows["omega_plot_output"])

        self.root.mainloop()
