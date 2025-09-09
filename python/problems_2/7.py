# Problem 7: Single Number (Find Unique)
# **Difficulty: ** Easy
# **Time:** 10 minutes
# **Pattern:** XOR properties
#
# Find the element that appears only once while all others appear twice.


def single_number(nums):
    """
    Find the single element (all others appear twice).

    Examples:
    Input: [2, 2, 1]
    Output: 1

    Input: [4, 1, 2, 1, 2]
    Output: 4

    Use O(1) space complexity.
    """
    # Your code here
    nums = sorted(nums)
    print(nums)
    if len(nums) == 1:
        return nums[0]
    for n in range(0, len(nums) - 1, 2):
        print(f"a: {nums[n]} b: {nums[n + 1]}")
        if nums[n] != nums[n + 1]:
            return nums[n]
    return nums[-1]


# Test cases
assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
assert single_number([3, 3, 7, 7, 10, 11, 11]) == 10
print("All tests passed!")
