# Problem 8: Count Set Bits (Hamming Weight)
# **Difficulty:** Easy
# **Time:** 10 minutes
# **Pattern:** Bit counting
#
# Count the number of 1's in the binary representation of a number.

def hamming_weight(n):
    """
    Count number of 1 bits in binary representation.

    Examples:
    Input: 11 (binary: 1011)
    Output: 3

    Input: 128 (binary: 10000000)
    Output: 1

    Input: 255 (binary: 11111111)
    Output: 8
    """
    # Your code here

    return list(bin(n))[2:].count('1')


# Test cases
assert hamming_weight(11) == 3
assert hamming_weight(128) == 1
assert hamming_weight(255) == 8
assert hamming_weight(0) == 0
assert hamming_weight(1) == 1
print("All tests passed!")
