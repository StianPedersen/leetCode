# Problem 9: Find All Anagrams

# **Pattern:** Sliding window with frequency map
#
# Find all starting indices of anagrams of a pattern in a string.

def find_anagrams(s, p):
    """
    Find all starting indices of p's anagrams in s.

    Examples:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0, 6]
    Explanation:
    - Substring at index 0: "cba" is anagram of "abc"
    - Substring at index 6: "bac" is anagram of "abc"

    Input: s = "abab", p = "ab"
    Output: [0, 1, 2]
    """
    # Your code here
    frequency_list = []
    size = len(p)

    def check_if_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    for it1 in range(len(s) - size + 1):
        string_1 = s[it1:size + it1]
        if check_if_anagram(string_1, p):
            frequency_list.append(it1)
    return frequency_list


# Test cases
assert find_anagrams("cbaebabacd", "abc") == [0, 6]
assert find_anagrams("abab", "ab") == [0, 1, 2]
assert find_anagrams("aaaa", "aa") == [0, 1, 2]
assert find_anagrams("abc", "xyz") == []
print("All tests passed!")
