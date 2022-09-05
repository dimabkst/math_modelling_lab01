from tkinter import *
from tkinter import ttk

MAX_DEFAULT_VALUE = 7 + 1


class results_output:

    def __init__(self, root, frame_column_row):

        self.results_output_frame = ttk.Frame(root, padding="3 3 12 12")
        self.results_output_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

        self.omega_output_frame = ttk.Frame(self.results_output_frame, padding="3 3 12 12")
        self.omega_output_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.solution_output_frame = ttk.Frame(self.results_output_frame, padding="3 3 12 12")
        self.solution_output_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.uniqueness_condition_output_frame = ttk.Frame(self.results_output_frame, padding="3 3 12 12")
        self.uniqueness_condition_output_frame.grid(column=0, row=2, sticky=(N, W, E, S))

        self.precision_output_frame = ttk.Frame(self.results_output_frame, padding="3 3 12 12")
        self.precision_output_frame.grid(column=0, row=3, sticky=(N, W, E, S))

    def receive_data_and_show_it(self, omega, solution, uniqueness_condition, precision):
        # Cleaning everything that was before
        for child in self.results_output_frame.winfo_children():
            for grandchild in child.winfo_children():
                grandchild.destroy()

        ttk.Label(self.omega_output_frame, text=f"{omega}").grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.solution_output_frame, text=f"{solution}").grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.uniqueness_condition_output_frame, text=f"{uniqueness_condition}").grid(column=0, row=0,
                                                                                               sticky=(N, W, E, S))
        ttk.Label(self.precision_output_frame, text=f"{precision}").grid(column=0, row=0, sticky=(N, W, E, S))
