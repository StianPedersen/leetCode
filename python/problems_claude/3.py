# Problem 3: Character Frequency Counter
# **Difficulty: ** Easy
# **Time: ** 10 minutes
# **Pattern: ** Using dictionary for counting
#
# Count the frequency of each character in a string and return the most frequent character(s).


def char_frequency(s):
    """
    Count character frequencies and find the most frequent character(s).

    Returns a tuple: (frequency_dict, list_of_most_frequent_chars)

    Example:
    Input: "programming"
    Output: ({'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}, ['r', 'g', 'm'])
    """
    return_dict = {}

    for l in s:
        if l not in return_dict.keys():
            return_dict[l] = 1
            # Test cases
        else:
            return_dict[l] += 1

    # Do the set thingy
    sorted_list = sorted(return_dict.items(), key=lambda val: val[1], reverse=True)
    sorted_list = [i[0] for i in sorted_list[:3]]
    return return_dict, sorted_list


freq, most = char_frequency("programming")
assert freq == {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
assert set(most) == {'r', 'g', 'm'}

freq, most = char_frequency("aabbcc")
assert freq == {'a': 2, 'b': 2, 'c': 2}
assert set(most) == {'a', 'b', 'c'}

freq, most = char_frequency("")
assert freq == {}
assert most == []

print("All tests passed!")
