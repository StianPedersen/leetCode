// #### Problem 2: Valid Parentheses
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Stack for matching pairs
//
// Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`,
// `'['` and `']'`, determine if the input string is valid.

#include <cassert>
#include <iostream>
#include <stack>
#include <string>

bool isValid(std::string s) {
  /*
  Check if parentheses/brackets/braces are valid.

  Examples:
  Input: "()"
  Output: true

  Input: "()[]{}"
  Output: true

  Input: "(]"
  Output: false
  */

  // Your code here
  return false;
}

int main() {
  assert(isValid("()") == true);
  assert(isValid("()[]{}") == true);
  assert(isValid("(]") == false);
  assert(isValid("([)]") == false);
  assert(isValid("{[]}") == true);
  assert(isValid("") == true);

  std::cout << "Problem 2: All tests passed!" << std::endl;
  return 0;
}
