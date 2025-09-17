// ####Problem 4 : Valid Palindrome **Difficulty : **Easy **Time
//     : **15 minutes **Pattern : **Two pointers +
//                                string manipulation
//
//                                    A phrase is a palindrome if,
//     after converting all uppercase letters into lowercase letters and
//             removing all non -
//         alphanumeric characters,
//     it reads the same forward and backward.

#include <cassert>
#include <cctype>
#include <iostream>
#include <print>
#include <string>
bool isPalindrome(std::string s) {
  /*
  Check if string is a palindrome (alphanumeric only, case-insensitive).

  Examples:
  Input: "A man, a plan, a canal: Panama"
  Output: true

  Input: "race a car"
  Output: false
  */

  // Your code here
  s.erase(
      std::remove_if(std::begin(s), std::end(s),
                     [](char const &c) -> bool { return !std::isalnum(c); }),
      std::end(s));
  auto it_b = std::begin(s);
  auto it_e = std::end(s) - 1;
  while (it_b <= it_e) {
    if (std::tolower(*it_e) != std::tolower(*it_b)) {
      return false;
    }
    it_e--;
    it_b++;
  }

  return true;
}

int main() {
  assert(isPalindrome("A man, a plan, a canal: Panama") == true);
  assert(isPalindrome("race a car") == false);
  assert(isPalindrome("Was it a car or a cat I saw?") == true);
  assert(isPalindrome("") == true);
  assert(isPalindrome("a") == true);

  std::cout << "Problem 4: All tests passed!" << std::endl;
  return 0;
}
