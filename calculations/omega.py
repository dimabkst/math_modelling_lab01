from sympy import Matrix, shape  # Using sympy, because don't like numpy
from typing import List, Set
from errors import BadMatrixEquationDimensionsError


# Returns x^ = (A+)b
def omega(A: List[list], b: list) -> Set[tuple]:  # Wanted lists but they are unhashable
    # A looks like [[a11, ..., a1n], ..., [am1, ..., amn]]
    # b looks like [b1, ..., bm]

    # Check whether A is m x n and b is m x 1
    if len(A) != len(b):
        raise BadMatrixEquationDimensionsError

    # Calculation of pseudo inverse matrix of A
    sympy_A = Matrix(A)
    sympy_b = Matrix(b)

    v_list = [Matrix([el for _ in range(shape(sympy_A)[1])]) for el in range(-2, 2 + 1, 1)]  # Vectors v with n entries
    sympy_omega = [sympy_A.pinv() * sympy_b + v - sympy_A.pinv() * sympy_A * v for v in v_list]

    # Preparing the result for set of tuples form
    res = {tuple(x[i, 0] for i in range(shape(sympy_A)[1])) for x in sympy_omega}

    return res
