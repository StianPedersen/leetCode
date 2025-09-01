# Problem 10: Valid Parentheses
# **Difficulty:** Easy
# **Time:** 15 minutes
# **Pattern:** Stack (bonus pattern)
#
# Check if a string containing parentheses, brackets, and braces is valid.

def is_valid_parentheses(s):
    """
    Check if parentheses/brackets/braces are valid.

    Examples:
    Input: "()"
    Output: True

    Input: "()[]{}"
    Output: True

    Input: "(]"
    Output: False

    Input: "([)]"
    Output: False
    """
    # Your code here
    pass


# Test cases
assert is_valid_parentheses("()")
assert is_valid_parentheses("()[]{}")
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("([)]") == False
assert is_valid_parentheses("{[]}")
assert is_valid_parentheses("")
print("All tests passed!")
