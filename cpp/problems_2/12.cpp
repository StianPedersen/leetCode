// #### Problem 12: Reverse String
//
// **Difficulty:** Easy
// **Time:** 10 minutes
// **Pattern:** Two pointers
//
// Write a function that reverses a string. The input string is given as an
// array of characters `s`. You must do this by modifying the input array
// in-place with O(1) extra memory.

#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

void reverseString(std::vector<char> &s) {
  /*
  Reverse string in-place.

  Examples:
  Input: s = ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]

  Input: s = ["H","a","n","n","a","h"]
  Output: ["h","a","n","n","a","H"]
  */
  // Your code here
  auto left_it = s.begin();
  auto right_it = s.end() - 1;

  while (left_it < right_it) {
    std::iter_swap(left_it, right_it);

    left_it++;
    right_it--;
  }
}

int main() {
  std::vector<char> s1 = {'h', 'e', 'l', 'l', 'o'};
  reverseString(s1);
  assert(s1 == std::vector<char>({'o', 'l', 'l', 'e', 'h'}));

  std::vector<char> s2 = {'H', 'a', 'n', 'n', 'a', 'h'};
  reverseString(s2);
  assert(s2 == std::vector<char>({'h', 'a', 'n', 'n', 'a', 'H'}));

  std::cout << "Problem 12: All tests passed!" << std::endl;
  return 0;
}
