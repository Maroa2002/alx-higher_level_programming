#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    a function that computes the square value of all integers in a matrix
    """
    if matrix is not None:
        square_matrix = []
        for row in matrix:
            square_values = map(lambda x: x ** 2, row)
            squared_list = list(square_values)
            square_matrix.append(squared_list)
        return square_matrix
