// #### Problem 5: First Unique Character
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Hash map for counting
//
// Given a string `s`, find the first non-repeating character in it and return
// its index. If it does not exist, return -1.

#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>

int firstUniqChar(std::string s) {
  /*
  Find the index of the first non-repeating character.

  Examples:
  Input: s = "leetcode"
  Output: 0 (character 'l' at index 0)

  Input: s = "loveleetcode"
  Output: 2 (character 'v' at index 2)
  */
  std::unordered_map<char, int> my_map;
  for (auto &c : s) {

    // std::cout << c << std::endl;
    if (auto search = my_map.find(c); search != my_map.end()) {
      my_map[c]++;
    } else {
      my_map.insert(std::make_pair(c, 1));
    }
  }
  for (size_t i = 0; i <= s.size(); i++) {
    if (my_map[s[i]] == 1)
      return i;
  }
  return -1;
}

int main() {
  assert(firstUniqChar("leetcode") == 0);
  assert(firstUniqChar("loveleetcode") == 2);
  assert(firstUniqChar("aabb") == -1);
  assert(firstUniqChar("z") == 0);
  assert(firstUniqChar("") == -1);

  std::cout << "Problem 5: All tests passed!" << std::endl;
  return 0;
}
