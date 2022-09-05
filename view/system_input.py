from tkinter import *
from tkinter import ttk

MAX_DEFAULT_VALUE = 7 + 1


class system_input:

    def __init__(self, root, frame_column_row):

        self.system_input_frame = ttk.Frame(root, padding="3 3 12 12")
        self.system_input_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

        self.matrix_input_frame = ttk.Frame(self.system_input_frame, padding="3 3 12 12")
        self.matrix_input_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.vector_b_input_frame = ttk.Frame(self.system_input_frame, padding="3 3 12 12")
        self.vector_b_input_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.matrix_row_shape_var = StringVar()
        self.matrix_row_shape_var.set("3")
        matrix_row_shape_combobox = ttk.Combobox(self.matrix_input_frame, textvariable=self.matrix_row_shape_var)
        matrix_row_shape_combobox.grid(column=0, row=0, sticky=W)
        matrix_row_shape_combobox['values'] = [f'{i}' for i in range(1, MAX_DEFAULT_VALUE)]
        matrix_row_shape_combobox.bind('<<ComboboxSelected>>', self.change_and_show_matrix)

        self.matrix_col_shape_var = StringVar()
        self.matrix_col_shape_var.set("3")
        matrix_col_shape_combobox = ttk.Combobox(self.matrix_input_frame, textvariable=self.matrix_col_shape_var)
        matrix_col_shape_combobox.grid(column=1, row=0, sticky=E)
        matrix_col_shape_combobox['values'] = [f'{i}' for i in range(1, MAX_DEFAULT_VALUE)]
        matrix_col_shape_combobox.bind('<<ComboboxSelected>>', self.change_and_show_matrix)

        self.matrix_vars = []
        self.matrix_entries = []
        self.vector_b_vars = []
        self.vector_b_entries = []

        for i in range(int(self.matrix_row_shape_var.get() or 0)):
            self.matrix_vars.append([])
            self.matrix_entries.append([])

            for j in range(int(self.matrix_col_shape_var.get() or 0)):
                self.matrix_vars[i].append(StringVar())
                self.matrix_vars[i][j].set("0")

                self.matrix_entries[i].append(ttk.Entry(self.matrix_input_frame,
                                                        textvariable=self.matrix_vars[i][j]))
                self.matrix_entries[i][j].grid(row=i + 1, column=j + 1, sticky=(N, W, E, S))

            self.vector_b_vars.append(StringVar())
            self.vector_b_vars[i].set("0")

            self.vector_b_entries.append(ttk.Entry(self.vector_b_input_frame, textvariable=self.vector_b_vars[i]))
            self.vector_b_entries[i].grid(row=i + 1, column=0, sticky=(N, W, E, S))

    def get_matrix(self):
        try:
            return [[int(self.matrix_vars[i][j].get()) for j in range(len(self.matrix_vars[0]))] for i in
                    range(len(self.matrix_vars))]
        except Exception as e:
            print(e)

    def get_vector_b(self):
        try:
            return [int(self.vector_b_vars[i].get()) for i in range(len(self.matrix_vars))]
        except Exception as e:
            print(e)

    def change_and_show_matrix(self, *args):
        try:
            old_matrix_row_shape = len(self.matrix_vars)
            old_matrix_col_shape = len(self.matrix_vars[0])

            for i in range(max(old_matrix_row_shape, int(self.matrix_row_shape_var.get() or 0))):
                if i >= min(old_matrix_row_shape, int(self.matrix_row_shape_var.get() or 0)):
                    if old_matrix_row_shape > int(self.matrix_row_shape_var.get() or 0):
                        self.matrix_vars = self.matrix_vars[0:i]
                        self.vector_b_vars = self.vector_b_vars[0:i]

                        for ii in range(i, old_matrix_row_shape):
                            self.vector_b_entries[ii].destroy()
                            for k in range(int(self.matrix_col_shape_var.get() or 0)):
                                self.matrix_entries[ii][k].destroy()

                        self.matrix_entries = self.matrix_entries[0:i]
                        self.vector_b_entries = self.vector_b_entries[0:i]
                        break
                    else:
                        self.matrix_vars.append([StringVar() for _ in range(int(self.matrix_col_shape_var.get() or 0))])
                        self.vector_b_vars.append(StringVar())

                        self.matrix_entries.append([
                            ttk.Entry(self.matrix_input_frame, textvariable=self.matrix_vars[i][k]) for k in
                            range(int(self.matrix_col_shape_var.get() or 0))])
                        self.vector_b_entries.append(
                            ttk.Entry(self.vector_b_input_frame, textvariable=self.vector_b_vars[i]))

                        for k in range(int(self.matrix_col_shape_var.get() or 0)):
                            self.matrix_vars[i][k].set("0")
                            self.matrix_entries[i][k].grid(row=i + 1, column=k + 1, sticky=(N, W, E, S))

                            self.vector_b_vars[i].set("0")
                            self.vector_b_entries[i].grid(row=i + 1, column=0, sticky=(N, W, E, S))

                for j in range(max(old_matrix_col_shape, int(self.matrix_col_shape_var.get() or 0))):
                    if j >= min(old_matrix_col_shape, int(self.matrix_col_shape_var.get() or 0)):
                        if old_matrix_col_shape > int(self.matrix_col_shape_var.get() or 0):
                            self.matrix_vars[i] = self.matrix_vars[i][0:j]
                            for k in range(j, old_matrix_col_shape):
                                self.matrix_entries[i][k].destroy()
                            self.matrix_entries[i] = self.matrix_entries[i][0:j]
                            break
                        else:
                            self.matrix_vars[i].append(StringVar())
                            self.matrix_vars[i][j].set("0")

                            self.matrix_entries[i].append(
                                ttk.Entry(self.matrix_input_frame, textvariable=self.matrix_vars[i][j]))
                            self.matrix_entries[i][j].grid(row=i + 1, column=j + 1, sticky=(N, W, E, S))
        except Exception as e:
            print(e)
