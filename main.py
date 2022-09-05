from errors import *
import calculations
from controller.start import start

try:
    # A = [[1, -1, 0], [-1, 2, 1], [2, -3, -1], [0, 1, 1]]
    # b = [6, 9, -9, 18]
    # print(calculations.p_inverse(A))
    # print(calculations.solve_linear_system(A, b))
    # print(calculations.precision(A, b))
    # print(calculations.omega(A, b))
    # print(calculations.uniqueness_condition(A))

    start()
except Exception as e:
    print(e)
