# # Problem 12: Container With Most Water
# **Difficulty: ** Medium
# **Time: ** 20 minutes
# **Pattern: ** Two pointers(optimization problem)
#
# Given an array of heights, find two lines that together with the x - axis
# form a container that holds the most water.


def max_water_container(heights):
    """
    Find maximum water that can be contained.

    Example:
    Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Explanation: Lines at index 1 (height=8) and index 8 (height=7)
                 form container with area = 7 * 7 = 49

    The area is calculated as:
    min(height[i], height[j]) * (j - i)
    """
    # Your code here
    pass


# Test cases
assert max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_water_container([1, 1]) == 1
assert max_water_container([4, 3, 2, 1, 4]) == 16
assert max_water_container([1, 2, 1]) == 2
print("All tests passed!")
