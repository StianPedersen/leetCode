# Problem 9: Merge Overlapping Intervals
# **Difficulty:** Medium
# **Time:** 15 minutes
# **Pattern:** Interval merging
#
# Given a list of intervals, merge all overlapping intervals.
#
def merge_intervals(intervals):
    """
    Merge overlapping intervals.

    Examples:
    Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]

    Input: [[1, 4], [4, 5]]
    Output: [[1, 5]]
    """
    # Your code here
    if len(intervals) == 0:
        return []
    ret_list = []
    skip = False
    for index, internal_list in enumerate(intervals[:-1]):
        if skip:
            skip = False
        elif internal_list[1] >= intervals[index + 1][0]:
            if internal_list[1] < intervals[index + 1][1]:
                ret_list.append([internal_list[0], intervals[index + 1][1]])
            else:
                ret_list.append([internal_list[0], internal_list[1]])
            skip = True
        else:
            ret_list.append(internal_list)
    if not skip:
        ret_list.append(intervals[-1])
    print(ret_list)
    return ret_list


# Test cases
assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
assert merge_intervals([[1, 4]]) == [[1, 4]]
assert merge_intervals([]) == []
print("All tests passed!")
