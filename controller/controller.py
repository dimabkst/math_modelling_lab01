import calculations


def receive_data_from_view(view):
    process_data_in_calculations(view, view.system_input.get_matrix(), view.system_input.get_vector_b())


def process_data_in_calculations(view, matrix, vector_b):
    omega = calculations.omega(matrix, vector_b)
    solution = calculations.solve_linear_system(matrix, vector_b)
    uniqueness_condition = calculations.uniqueness_condition(matrix)
    precision = calculations.precision(matrix, vector_b)
    give_date_to_output(view, omega, solution, uniqueness_condition, precision)


def give_date_to_output(view, omega, solution, uniqueness_condition, precision):
    view.results_output.receive_data_and_show_it(omega, solution, uniqueness_condition, precision)
    view.omega_plot_output.receive_data_and_show_plot(omega)


