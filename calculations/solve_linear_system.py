from sympy import Matrix, shape  # Using sympy, because don't like numpy
from typing import List
from errors import BadMatrixEquationDimensionsError


# Returns x^ = (A+)b
def solve_linear_system(A: List[list], b: list) -> list:
    # A looks like [[a11, ..., a1n], ..., [am1, ..., amn]]
    # b looks like [b1, ..., bm]

    # Check whether A is m x n and b is m x 1
    if len(A) != len(b):
        raise BadMatrixEquationDimensionsError

    # Calculation of pseudo inverse matrix of A
    sympy_A = Matrix(A)
    sympy_b = Matrix(b)

    sympy_x = sympy_A.pinv() * sympy_b

    # Preparing the result for list form
    res = [float(sympy_x[i, 0]) for i in range(shape(sympy_x)[0])]  # shape returns (m, n), m - num of rows, n - of cols

    return res
