# Problem 1: Spiral Matrix Traversal
# **Difficulty:** Medium
# **Time:** 20 minutes
# **Pattern:** Matrix traversal with boundaries
#
# Given an m x n matrix, return all elements of the matrix in spiral order (clockwise from outside to center).

def spiral_order(matrix):
    """
    Traverse matrix in spiral order.

    Examples:
    Input: [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    Input: [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Input:  [1,     2,      3,      4],
            [5,     6,      7,      8],
            [9,     10,     11,     12]]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    mylist: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 6]
    """
    # Your code here
    res_list = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        # Moving right
        for col in range(left, right + 1):
            res_list.append(matrix[top][col])
        top += 1

        # Moving down
        for row in range(top, bottom + 1):
            res_list.append(matrix[row][right])
        right -= 1

        # Moving left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                res_list.append(matrix[bottom][col])
            bottom -= 1

        # Moving up
        if left <= right:
            for row in range(bottom, top - 1, -1):
                res_list.append(matrix[row][left])
            left += 1

    print("Res_list: ", res_list)
    return res_list


# Test cases
assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_order([[1]]) == [1]
assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
print("All tests passed!")
