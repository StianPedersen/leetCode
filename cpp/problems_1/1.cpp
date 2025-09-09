// #### Problem 1: Two Sum
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Hash map for complement lookup
//
// Given an array of integers `nums` and an integer `target`, return indices of
// the two numbers such that they add up to `target`.

#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(std::vector<int> &nums, int target) {
  /*
  Find two numbers that add up to target and return their indices.

  Examples:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1] (nums[0] + nums[1] = 2 + 7 = 9)

  Input: nums = [3,2,4], target = 6
  Output: [1,2] (nums[1] + nums[2] = 2 + 4 = 6)
  */

  // Your code here
  for (auto &e : nums) {
    auto to_find = target - e;
    std::cout << "To find " << to_find << std::endl;
  }
  return {};
}

int main() {
  std::vector<int> nums1 = {2, 7, 11, 15};
  std::vector<int> result1 = twoSum(nums1, 9);
  assert(result1.size() == 2 && result1[0] == 0 && result1[1] == 1);

  std::vector<int> nums2 = {3, 2, 4};
  std::vector<int> result2 = twoSum(nums2, 6);
  assert(result2.size() == 2 && result2[0] == 1 && result2[1] == 2);
  //
  std::cout << "Problem 1: All tests passed!" << std::endl;
  return 0;
}
