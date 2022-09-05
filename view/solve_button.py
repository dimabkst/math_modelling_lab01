from tkinter import *
from tkinter import ttk
from controller.controller import receive_data_from_view


class solve_button:

    def __init__(self, root, frame_column_row, view):

        self.solve_button_frame = ttk.Frame(root, padding="3 3 12 12")
        self.solve_button_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))
        self.solve_button = ttk.Button(self.solve_button_frame, text='Solve system',
                                       command=lambda: receive_data_from_view(view))
        self.solve_button.grid(column=0, row=0, sticky=(N, W, E, S))

        root.bind('<Return>', lambda e: self.solve_button.invoke())
