#!/usr/bin/python3
"""contains a method that divides all elements of a matrix
Args: matrix - input matrix
      div - divisor
return: new_matrix with results
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    message = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(message)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(message)

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be an integer')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
