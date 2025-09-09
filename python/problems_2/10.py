# Problem 10: Insert Interval
# **Difficulty:** Medium
# **Time:** 20 minutes
# **Pattern:** Interval manipulation
#
# Insert a new interval into a sorted list of non-overlapping intervals and merge if necessary.
#
def insert_interval(intervals, new_interval):
    """
    Insert new interval and merge if necessary.

    Examples:
    Input: intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
    Output: [[1, 5], [6, 9]]

    Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
           new_interval = [4, 8]
    Output: [[1, 2], [3, 10], [12, 16]]
    """
    i = 0
    n = len(intervals)
    result_list = []
    while i < n and new_interval[0] > intervals[i][1]:
        result_list.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    result_list.append(new_interval)

    while i < n:
        result_list.append(intervals[i])
        i += 1

    print(result_list)
    return result_list


# Test cases
assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert insert_interval([], [5, 7]) == [[5, 7]]
assert insert_interval([[1, 5]], [2, 3]) == [[1, 5]]
print("All tests passed!")
