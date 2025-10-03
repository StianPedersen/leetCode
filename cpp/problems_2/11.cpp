// #### Problem 11: Move Zeroes
//
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Two pointers technique
//
// Given an integer array `nums`, move all 0's to the end of it while
// maintaining the relative order of the non-zero elements.

#include <cassert>
#include <iostream>
#include <vector>

void moveZeroes(std::vector<int> &nums) {
  /*
  Move all zeros to end while maintaining order of non-zeros.

  Examples:
  Input: nums = [0,1,0,3,12]
  Output: [1,3,12,0,0]

  Input: nums = [0]
  Output: [0]
  */

  // Your code here
}

int main() {
  std::vector<int> nums1 = {0, 1, 0, 3, 12};
  moveZeroes(nums1);
  assert(nums1 == std::vector<int>({1, 3, 12, 0, 0}));

  std::vector<int> nums2 = {0};
  moveZeroes(nums2);
  assert(nums2 == std::vector<int>({0}));

  std::vector<int> nums3 = {1, 2, 3};
  moveZeroes(nums3);
  assert(nums3 == std::vector<int>({1, 2, 3}));

  std::cout << "Problem 11: All tests passed!" << std::endl;
  return 0;
}
