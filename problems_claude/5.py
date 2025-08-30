# Problem 5: Valid Palindrome (with cleaning)
# **Difficulty: ** Easy
# **Time: ** 15 minutes
# **Pattern: ** String manipulation + two - pointer
#
# Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.
#


import enum


def is_valid_palindrome(s):
    """
    Check if string is a palindrome (alphanumeric only, case-insensitive).

    Examples:
    Input: "A man, a plan, a canal: Panama"
    Output: True

    Input: "race a car"
    Output: False
    """
    # Your code here
    s = list(filter(lambda x: x.isalnum(), s))
    back_pos = len(s) - 1
    for i, c in enumerate(s):
        if i == (back_pos - i):
            print(f"Break {c} - {s[back_pos - i]}")
            break
        if c.lower() == s[back_pos - i].lower():
            pass
        else:
            return False
    return True


# Test cases
assert is_valid_palindrome("A man, a plan, a canal: Panama")
assert is_valid_palindrome("race a car") == False
assert is_valid_palindrome("Was it a car or a cat I saw?")
assert is_valid_palindrome("")
assert is_valid_palindrome("a")
print("All tests passed!")
