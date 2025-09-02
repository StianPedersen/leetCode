# Problem 2: Rotate Matrix 90 Degrees
# **Difficulty: ** Medium
# **Time: ** 15 minutes
# **Pattern: ** In - place matrix manipulation
#
# Rotate an n x n matrix 90 degrees clockwise in -place(modify the original matrix).

def rotate_matrix(matrix):
    """
    Rotate matrix 90 degrees clockwise in-place.

    Example:
    Input: [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    Transpose:
            [[1, 4, 7],
             [2, 5, 8],
             [3, 6, 9]]

    After rotation: [[7, 4, 1],
                     [8, 5, 2],
                     [9, 6, 3]]


    Note: Modify the matrix in-place and return it.
    """
    # Your code here
    # Transpose matrix
    length = len(matrix[0])
    depth = len(matrix)
    print("M_before: ", matrix)
    for x in range(length):
        for y in range(x, depth):
            tmp_2 = matrix[y][x]
            matrix[y][x] = matrix[x][y]  # tmp
            matrix[x][y] = tmp_2

    for row in matrix:
        row.reverse()
    return matrix


# Test cases
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix1)
assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix2 = [[1, 2], [3, 4]]
rotate_matrix(matrix2)
assert matrix2 == [[3, 1], [4, 2]]

matrix3 = [[1]]
rotate_matrix(matrix3)
assert matrix3 == [[1]]

print("All tests passed!")
