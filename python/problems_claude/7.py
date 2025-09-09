# Problem 7: Two Sum in Sorted Array
# **Difficulty:** Easy
# **Time:** 15 minutes
# **Pattern:** Two pointers (opposite direction)
#
# Given a sorted array and a target sum, find two numbers that add up to the target. Return their indices.
#

def two_sum_sorted(arr, target):
    """
    Find two numbers in sorted array that sum to target.

    Examples:
    Input: arr = [2, 7, 11, 15], target = 9
    Output: [0, 1] (indices of 2 and 7)

    Input: arr = [2, 3, 4], target = 6
    Output: [0, 2] (indices of 2 and 4)

    Return empty list if no solution exists.
    """
    # Your code here
    for ptr_1 in range(len(arr)):
        ptr_2 = ptr_1 + 1
        while ptr_2 < len(arr):
            if arr[ptr_1] + arr[ptr_2] == target:
                return [ptr_1, ptr_2]
            else:
                ptr_2 += 1
    return []


# Test cases
assert two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_sorted([2, 3, 4], 6) == [0, 2]
assert two_sum_sorted([1, 2, 3, 4], 10) == []
assert two_sum_sorted([1, 2], 3) == [0, 1]
print("All tests passed!")
