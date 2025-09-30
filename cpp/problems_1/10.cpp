// #### Problem 10: Contains Duplicate
//
// **Difficulty:** Easy
// **Time:** 10 minutes
// **Pattern:** Hash set for uniqueness check
//
// Given an integer array `nums`, return `true` if any value appears at least
// twice in the array, and return `false` if every element is distinct.
//
#include <cassert>
#include <iostream>
#include <unordered_set>
#include <vector>

bool containsDuplicate(std::vector<int> &nums) {
  /*
  Check if array contains any duplicate values.

  Examples:
  Input: nums = [1,2,3,1]
  Output: true

  Input: nums = [1,2,3,4]
  Output: false

  Input: nums = [1,1,1,3,3,4,3,2,4,2]
  Output: true
  */

  // Your code here
  std::unordered_set<int> my_set;

  for (auto var : nums) {
    if (my_set.count(var) == 1) {
      return true;
    } else {
      my_set.insert(var);
    }
  }
  return false;
}

int main() {
  std::vector<int> nums1 = {1, 2, 3, 1};
  assert(containsDuplicate(nums1) == true);

  std::vector<int> nums2 = {1, 2, 3, 4};
  assert(containsDuplicate(nums2) == false);

  std::vector<int> nums3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
  assert(containsDuplicate(nums3) == true);

  std::vector<int> nums4 = {};
  assert(containsDuplicate(nums4) == false);

  std::cout << "Problem 10: All tests passed!" << std::endl;
  return 0;
}
