// #### Problem 3: Remove Duplicates from Sorted Array
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Two pointers technique
//
// Given an integer array `nums` sorted in non-decreasing order, remove the
// duplicates in-place such that each unique element appears only once.

#include <cassert>
#include <iostream>
#include <print>
#include <vector>

int removeDuplicates(std::vector<int> &nums) {
  /*
  Remove duplicates from sorted array in-place.

  Examples:
  Input: nums = [1,1,2]
  Output: 2, nums = [1,2,_]

  Input: nums = [0,0,1,1,1,2,2,3,3,4]
  Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
  */

  // Your code here
  for (auto it = std::begin(nums) + 1; it != end(nums);) {
    if (*it == *(it - 1)) {
      nums.erase(it);
    } else {
      it++;
    }
  }
  return nums.size();
}

int main() {
  std::vector<int> nums1 = {1, 1, 2};
  int len1 = removeDuplicates(nums1);
  assert(len1 == 2);
  assert(nums1[0] == 1 && nums1[1] == 2);

  std::vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
  int len2 = removeDuplicates(nums2);
  assert(len2 == 5);
  assert(nums2[0] == 0 && nums2[1] == 1 && nums2[2] == 2 && nums2[3] == 3 &&
         nums2[4] == 4);

  std::cout << "Problem 3: All tests passed!" << std::endl;
  return 0;
}
