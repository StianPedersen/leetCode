# Problem 2: Move Zeros to End
# **Difficulty:** Easy
# **Time:** 15 minutes
# **Pattern:** Two-pointer technique (same direction)

# Move all zeros in an array to the end while maintaining the relative order of non-zero elements.

def move_zeros_to_end(arr):
    """
    Move all zeros to the end of the array while maintaining order of non-zero elements.

    Examples:
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

    Input: [0, 0, 1]
    Output: [1, 0, 0]
    """
    # Your code here
    n = len(arr)
    ret_array = [0] * n
    pos_pointer = 0
    for i in range(n):
        if arr[i] != 0:
            ret_array[pos_pointer] = arr[i]
            pos_pointer += 1

    print(f"ARRAY: {ret_array}")
    return ret_array


# Test cases
assert move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros_to_end([0, 0, 1]) == [1, 0, 0]
assert move_zeros_to_end([1, 2, 3]) == [1, 2, 3]
assert move_zeros_to_end([0]) == [0]
print("All tests passed!")
