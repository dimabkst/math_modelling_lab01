from tkinter import *
from tkinter import ttk


class results_output:

    def __init__(self, root, frame_column_row):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white",  borderwidth=5, relief='raised')
        s.configure("VectorWhiteBg.TFrame", background="white", borderwidth=5, relief="solid")
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        # Frames
        self.results_output_frame = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.results_output_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

        self.omega_output_frame = ttk.Frame(self.results_output_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.omega_output_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.solution_output_frame = ttk.Frame(self.results_output_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.solution_output_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.uniqueness_condition_output_frame = ttk.Frame(self.results_output_frame, style="WhiteBg.TFrame",
                                                           padding="3 3 12 12")
        self.uniqueness_condition_output_frame.grid(column=0, row=2, sticky=(N, W, E, S))

        self.precision_output_frame = ttk.Frame(self.results_output_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.precision_output_frame.grid(column=0, row=3, sticky=(N, W, E, S))
        #

        # Align
        self.align_rows_cols(self.results_output_frame)
        #

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def receive_data_and_show_it(self, omega, solution, uniqueness_condition, precision):
        # Cleaning everything that was before
        for child in self.results_output_frame.winfo_children():
            for grandchild in child.winfo_children():
                grandchild.destroy()

        # Omega
        ttk.Label(self.omega_output_frame, text="Ωx = ", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, W, E, S))
        i = 0
        for vector in omega:
            temp_vector_frame = ttk.Frame(self.omega_output_frame, style="VectorWhiteBg.TFrame", padding="3 3 12 12")
            temp_vector_frame.grid(column=i + 1, row=0, sticky=(N, W, E, S))
            for j in range(len(vector)):
                ttk.Label(temp_vector_frame, text=f"{vector[j]}", style="WhiteBg.TLabel") \
                    .grid(column=0, row=j, sticky=(N, W, E, S))
            i += 1
        #

        # Solution
        ttk.Label(self.solution_output_frame, text="x̂ = ", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, W, E, S))
        temp_vector_frame = ttk.Frame(self.solution_output_frame, style="VectorWhiteBg.TFrame", padding="3 3 12 12")
        temp_vector_frame.grid(column=1, row=0, sticky=(N, W, E, S))
        for i in range(len(solution)):
            ttk.Label(temp_vector_frame, text=f"{solution[i]}", style="WhiteBg.TLabel") \
                .grid(column=0, row=i, sticky=(N, W, E, S))
        #

        # Uniqueness_condition
        ttk.Label(self.uniqueness_condition_output_frame, text="Умова однозначності —", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.uniqueness_condition_output_frame, text=f"{uniqueness_condition}", style="WhiteBg.TLabel") \
            .grid(column=1, row=0, sticky=(N, W, E, S))
        #

        # Precision
        ttk.Label(self.precision_output_frame, text="Точність розв'язку: ɛ² =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.precision_output_frame, text=f"{precision}", style="WhiteBg.TLabel") \
            .grid(column=1, row=0, sticky=(N, W, E, S))
        #

# Somewhy does not work
# def clean_child(frame):
#     while frame.winfo_children():
#         for child in frame.winfo_children():
#             clean_child(child)
#             child.destroy()
