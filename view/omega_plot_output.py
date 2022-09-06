from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class omega_plot_output:

    def __init__(self, root, frame_column_row):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")

        self.omega_plot_output_frame = ttk.Frame(root, padding="3 3 12 12", style="TopWhiteBg.TFrame")
        self.omega_plot_output_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

    def receive_data_and_show_plot(self, omega):
        # Cleaning everything that was before
        for child in self.omega_plot_output_frame.winfo_children():
            child.destroy()

        if omega and 2 <= len(list(omega)[0]) <= 3:

            fig = Figure(figsize=(10, 5), dpi=75)
            fig.patch.set_facecolor('white')

            omega_points = {tuple(float(el) for el in point) for point in omega}  # Had SymPy numbers before

            colors = ['k', 'b', 'g', 'r', 'm', 'c', 'y']

            if len(list(omega)[0]) == 2:
                x_coords = [point[0] for point in omega_points]
                y_coords = [point[1] for point in omega_points]

                plot = fig.add_subplot(111)
                for i in range(len(omega_points)):
                    plot.plot(x_coords[i], y_coords[i], f"{colors[i % len(colors)]}.")
            else:  # == 3
                x_coords = [point[0] for point in omega_points]
                y_coords = [point[1] for point in omega_points]
                z_coords = [point[2] for point in omega_points]

                plot = fig.add_subplot(111, projection="3d")
                for i in range(len(omega_points)):
                    plot.plot(x_coords[i], y_coords[i], z_coords[i], f"{colors[i % len(colors)]}.")

            # creating the Tkinter canvas containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig, master=self.omega_plot_output_frame)
            canvas.get_tk_widget().configure(bg="white")
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()

            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, self.omega_plot_output_frame)
            toolbar.winfo_children()[-2].config(background="white")
            toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()
