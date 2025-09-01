# Problem 11: Group Anagrams
# ** Difficulty: ** Medium
# **Time:** 20 minutes
# **Pattern:** Hash map with sorted key
# Group strings that are anagrams of each other.


def group_anagrams(strs):
    """
    Group strings that are anagrams of each other.

    Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

    Note: Order of groups and order within groups may vary.
    """
    # Your code here
    hash_map = {}

    for s in strs:
        s_tmp = "".join(sorted(s.lower()))
        if s_tmp in hash_map:
            hash_map[s_tmp].append(s)
        else:
            hash_map[s_tmp] = [s]
    ret_list = []

    for key, value in hash_map.items():
        ret_list.append(value)

    return ret_list


# Test cases
result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Convert to sets for comparison (order doesn't matter)
result_sets = [set(group) for group in result]
expected_sets = [set(group) for group in expected]
assert sorted(result_sets, key=str) == sorted(expected_sets, key=str)

result = group_anagrams([""])
assert result == [[""]]

result = group_anagrams(["a"])
assert result == [["a"]]

print("All tests passed!")
