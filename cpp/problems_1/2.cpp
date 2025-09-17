// #### Problem 2: Valid Parentheses
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Stack for matching pairs
//
// Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`,
// `'['` and `']'`, determine if the input string is valid.

#include <cassert>
#include <iostream>
#include <map>
#include <print>
#include <stack>
#include <string>
#include <vector>
using namespace std;

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
  stack<char> my_stack;
  vector<char> left_chars = {'(', '{', '['};
  map<char, char> the_map = {{')', '('}, {'}', '{'}, {']', '['}};
  for (std::string::iterator it = s.begin(); it != s.end(); ++it) {
    bool found =
        find(left_chars.begin(), left_chars.end(), *it) != left_chars.end();
    if (found) {
      my_stack.push(*it);
    } else {
      char to_check = my_stack.top();
      my_stack.pop();
      if (the_map[*it] != to_check) {
        return false;
      }
    }
  }

  return true;
}

int main() {
  std::println("hello world");
  assert(isValid("()") == true);
  assert(isValid("()[]{}") == true);
  assert(isValid("(]") == false);
  assert(isValid("([)]") == false);
  assert(isValid("{[]}") == true);
  assert(isValid("") == true);

  std::cout << "Problem 2: All tests passed!" << std::endl;
  return 0;
}
