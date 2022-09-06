from sympy import Matrix, shape  # Using sympy, because don't like numpy
from typing import List


def p_inverse(A: List[list]) -> List[list]:  # Use list of lists for Matrix => it 100% is compatible with everything
    # A looks like [[a11, ..., a1n], ..., [am1, ..., amn]]

    # Calculation of pseudo inverse matrix of A
    sympy_A = Matrix(A)
    sympy_p_inversed_A = sympy_A.pinv()

    # Preparing the result for list of lists form
    res = [list(sympy_p_inversed_A.row(i)) for i in
           range(shape(sympy_p_inversed_A)[0])]  # shape returns (m, n), m - num of rows, n - of cols

    # If you need list of lists of floats, but Tkinter shows SymPy numbers well, so I do not do this
    # res = [[float(el) for el in res[i]] for i in range(len(res))]
    return res
