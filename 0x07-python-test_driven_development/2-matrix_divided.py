#!/usr/bin/python3
"""
Module 2-matrix_divided
divides all elements of a matrix by 2,
matrix elements must be either float or int
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with all elements from original matrix
     divided by 2
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    len_row = 0
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    for elements in matrix:
        if type(elements) is not list:
            raise TypeError(msg_type)
        if len_row != 0 and len(elements) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        len_row = len(elements)
        new_list = []
        for i in elements:
            if not isinstance(i, (int, float)):
                raise TypeError(msg_type)
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
