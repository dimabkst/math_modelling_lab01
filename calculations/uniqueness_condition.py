from sympy import Matrix, shape  # Using sympy, because don't like numpy
from typing import List


def uniqueness_condition(A: List[list]) -> bool:
    # A looks like [[a11, ..., a1n], ..., [am1, ..., amn]]

    sympy_A = Matrix(A)

    res = (sympy_A.transpose() * sympy_A).det() > 0

    return res
