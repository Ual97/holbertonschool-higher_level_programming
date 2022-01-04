#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for rows in matrix:
        new_m.append(list(map(lambda x: x**2, rows)))
    return (new_m)
