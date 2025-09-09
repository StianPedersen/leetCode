# Problem 8: Maximum Subarray Sum (Fixed Size)

# **Pattern:** Fixed-size sliding window

# Find the maximum sum of any contiguous subarray of size k.

def max_subarray_sum_fixed(arr, k):
    """
    Find maximum sum of any subarray of size k.

    Examples:
    Input: arr = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9 (subarray [5, 1, 3])

    Input: arr = [2, 3, 4, 1, 5], k = 2
    Output: 7 (subarray [3, 4])
    """
    # Your code here
    size = k
    sum = 0
    for it1 in range(0, len(arr) - size + 1):
        temp_sum = arr[it1]

        for it2 in range(1, size):
            temp_sum = temp_sum + arr[it2 + it1]

        if sum < temp_sum:
            sum = temp_sum
    return sum


# Test cases
assert max_subarray_sum_fixed([2, 1, 5, 1, 3, 2], 3) == 9
assert max_subarray_sum_fixed([2, 3, 4, 1, 5], 2) == 7
assert max_subarray_sum_fixed([1], 1) == 1
assert max_subarray_sum_fixed([1, 2, 3], 4) == 0  # k > array length
print("All tests passed!")
