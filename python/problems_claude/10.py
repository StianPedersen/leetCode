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
    stack = []
    p_mapping = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in p_mapping:
            # It is a closing bracket
            if len(stack) == 0:
                return False
            if stack[-1] != p_mapping[c]:
                return False
            stack.pop()
        else:
            stack.append(c)

    return len(stack) == 0


# Test cases
assert is_valid_parentheses("()")
assert is_valid_parentheses("()[]{}")
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("([)]") == False
assert is_valid_parentheses("{[]}")
assert is_valid_parentheses("")
print("All tests passed!")
