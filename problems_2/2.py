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

    After rotation: [[7, 4, 1],
                     [8, 5, 2],
                     [9, 6, 3]]

    Note: Modify the matrix in-place and return it.
    """
    # Your code here
    pass


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
