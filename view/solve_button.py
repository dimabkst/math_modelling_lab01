from tkinter import *
from tkinter import ttk
from controller.controller import receive_data_from_view


class solve_button:

    def __init__(self, root, frame_column_row, view):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white",  borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")

        self.solve_button_frame = ttk.Frame(root, padding="3 3 12 12", style="TopWhiteBg.TFrame")
        self.solve_button_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

        self.solve_button = ttk.Button(self.solve_button_frame, text='Solve system',
                                       command=lambda: receive_data_from_view(view))
        self.solve_button.grid(column=0, row=0, sticky=(N, W, E, S))

        self.align_rows_cols(self.solve_button_frame)

        root.bind('<Return>', lambda e: self.solve_button.invoke())

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
