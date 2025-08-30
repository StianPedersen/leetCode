# Problem
# **Difficulty: ** Easy
# **Time: ** 15 minutes
# **Pattern: ** Array traversal with edge cases
#
# Given an array of integers, create a new array where each element is the sum of itself and its immediate neighbors.
# Handle edge cases for first and last elements.
#
# ```python
#
#
def neighbor_sum(arr: list[int]) -> list[int]:
    """
    Create an array where each element is the sum of itself and its neighbors.

    Examples:
    Input: [1, 2, 3, 4, 5]
    Output: [3, 6, 9, 12, 9]

    Explanation:
    - arr[0]: 1 + 2 = 3 (no left neighbor)
    - arr[1]: 1 + 2 + 3 = 6
    - arr[2]: 2 + 3 + 4 = 9
    - arr[3]: 3 + 4 + 5 = 12
    - arr[4]: 4 + 5 = 9 (no right neighbor)
    """
    # Your code here
    return_array = []
    for i, value in enumerate(arr):
        if i == 0 and len(arr) == 1:
            return_array = arr
        elif i == 0:
            return_array.append(value + arr[i + 1])
        elif i == len(arr) - 1:
            return_array.append(value + arr[i - 1])
        else:
            return_array.append(arr[i - 1] + value + arr[i + 1])
    return return_array


# Test cases
assert neighbor_sum([1, 2, 3, 4, 5]) == [3, 6, 9, 12, 9]
assert neighbor_sum([10]) == [10]
assert neighbor_sum([5, 1]) == [6, 6]
assert neighbor_sum([]) == []
print("All tests passed!")

#
#
#
#
#
#
