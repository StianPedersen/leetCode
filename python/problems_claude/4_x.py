# Problem 4: First Non-Repeating Character
# **Difficulty:** Easy-Medium
# **Time:** 15 minutes
# **Pattern:** Hash map for frequency + two-pass technique
#
# Find the first non-repeating character in a string. Return its index, or -1 if none exists.

def first_non_repeating(s):
    """
    Find the index of the first non-repeating character.

    Examples:
    Input: "leetcode"
    Output: 0 (character 'l' at index 0)

    Input: "loveleetcode"
    Output: 2 (character 'v' at index 2)

    Input: "aabb"
    Output: -1 (no non-repeating character)
    """
    # Your code here
    a_dict = {}
    for c in s:
        if c not in a_dict:
            a_dict[c] = 1
        else:
            a_dict[c] += 1

    for i, (key, value) in enumerate(a_dict.items()):
        if value == 1:
            return i
    return -1


# Test cases
assert first_non_repeating("leetcode") == 0
assert first_non_repeating("loveleetcode") == 2
assert first_non_repeating("aabb") == -1
assert first_non_repeating("z") == 0
assert first_non_repeating("") == -1
print("All tests passed!")
