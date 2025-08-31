# Problem 6: Longest Substring Without Repeating Characters
# **Difficulty: ** Medium
# **Time: ** 20 minutes
# **Pattern: ** Sliding window with hash map
#
# Find the length of the longest substring without repeating characters.

from re import sub


def longest_unique_substring(s):
    """
        Find the length of the longest substring without repeating characters.

        Examples:
        Input: "abcabcbb"
        Output: 3 (substring "abc")

        Input: "bbbbb"
        Output: 1 (substring "b")

        Input: "pwwkew"
        Output: 3 (substring "wke" or "kew")
        """

    # Your code here
    char_list = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        current_character = s[end]

        if current_character in char_list and char_list[current_character] >= start:
            start = char_list[current_character] + 1

        char_list[current_character] = end
        current_length = end - start + 1

        max_length = max(max_length, current_length)

    return max_length


# Test cases
assert longest_unique_substring("abcabcbb") == 3
assert longest_unique_substring("bbbbb") == 1
assert longest_unique_substring("pwwkew") == 3
assert longest_unique_substring("") == 0
assert longest_unique_substring("dvdf") == 3
assert longest_unique_substring("abcdef") == 6
print("All tests passed!")
