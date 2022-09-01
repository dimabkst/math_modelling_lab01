from sympy import Matrix  # Using sympy, because don't like numpy
from typing import List
from errors import BadMatrixEquationDimensionsError


def precision(A: List[list], b: list) -> float:
    # A looks like [[a11, ..., a1n], ..., [am1, ..., amn]]
    # b looks like [b1, ..., bm]

    # Check whether A is m x n and b is m x 1
    if len(A) != len(b):
        raise BadMatrixEquationDimensionsError

    # Calculation of pseudo inverse matrix of A
    sympy_A = Matrix(A)
    sympy_b = Matrix(b)

    sympy_precision = sympy_b.transpose() * sympy_b - sympy_b.transpose() * sympy_A * sympy_A.pinv() * sympy_b

    # Preparing the result for float form
    res = float(sympy_precision[0, 0])

    return res
