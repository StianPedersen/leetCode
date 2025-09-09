# LeetCode C++ Easy Problems - Practice Set 1

## Week 1: Fundamental Patterns

### Day 1-2: Array and Hash Map Basics

#### Problem 1: Two Sum
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Hash map for complement lookup

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

```cpp
#include <vector>
#include <unordered_map>
#include <iostream>
#include <cassert>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    /*
    Find two numbers that add up to target and return their indices.
    
    Examples:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (nums[0] + nums[1] = 2 + 7 = 9)
    
    Input: nums = [3,2,4], target = 6  
    Output: [1,2] (nums[1] + nums[2] = 2 + 4 = 6)
    */
    
    // Your code here
    return {};
}

int main() {
    std::vector<int> nums1 = {2, 7, 11, 15};
    std::vector<int> result1 = twoSum(nums1, 9);
    assert(result1.size() == 2 && result1[0] == 0 && result1[1] == 1);
    
    std::vector<int> nums2 = {3, 2, 4};
    std::vector<int> result2 = twoSum(nums2, 6);
    assert(result2.size() == 2 && result2[0] == 1 && result2[1] == 2);
    
    std::cout << "Problem 1: All tests passed!" << std::endl;
    return 0;
}
```

#### Problem 2: Valid Parentheses
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Stack for matching pairs

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

```cpp
#include <string>
#include <stack>
#include <iostream>
#include <cassert>

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
```

#### Problem 3: Remove Duplicates from Sorted Array
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Two pointers technique

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

```cpp
#include <vector>
#include <iostream>
#include <cassert>

int removeDuplicates(std::vector<int>& nums) {
    /*
    Remove duplicates from sorted array in-place.
    
    Examples:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    */
    
    // Your code here
    return 0;
}

int main() {
    std::vector<int> nums1 = {1, 1, 2};
    int len1 = removeDuplicates(nums1);
    assert(len1 == 2);
    assert(nums1[0] == 1 && nums1[1] == 2);
    
    std::vector<int> nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int len2 = removeDuplicates(nums2);
    assert(len2 == 5);
    assert(nums2[0] == 0 && nums2[1] == 1 && nums2[2] == 2 && nums2[3] == 3 && nums2[4] == 4);
    
    std::cout << "Problem 3: All tests passed!" << std::endl;
    return 0;
}
```

### Day 3-4: String Operations

#### Problem 4: Valid Palindrome
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Two pointers + string manipulation

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

```cpp
#include <string>
#include <cctype>
#include <iostream>
#include <cassert>

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
    return false;
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
```

#### Problem 5: First Unique Character
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Hash map for counting

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

```cpp
#include <string>
#include <unordered_map>
#include <iostream>
#include <cassert>

int firstUniqChar(std::string s) {
    /*
    Find the index of the first non-repeating character.
    
    Examples:
    Input: s = "leetcode"
    Output: 0 (character 'l' at index 0)
    
    Input: s = "loveleetcode"
    Output: 2 (character 'v' at index 2)
    */
    
    // Your code here
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
```

### Day 5-6: Linked Lists and Arrays

#### Problem 6: Merge Two Sorted Lists
**Difficulty:** Easy  
**Time:** 20 minutes  
**Pattern:** Two pointers on linked lists

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list.

```cpp
#include <vector>
#include <iostream>
#include <cassert>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    /*
    Merge two sorted linked lists.
    
    Examples:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
    Input: list1 = [], list2 = []
    Output: []
    */
    
    // Your code here
    return nullptr;
}

// Helper function to create list from vector
ListNode* createList(std::vector<int> vals) {
    ListNode dummy(0);
    ListNode* current = &dummy;
    for (int val : vals) {
        current->next = new ListNode(val);
        current = current->next;
    }
    return dummy.next;
}

// Helper function to convert list to vector
std::vector<int> listToVector(ListNode* head) {
    std::vector<int> result;
    while (head) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

int main() {
    ListNode* list1 = createList({1, 2, 4});
    ListNode* list2 = createList({1, 3, 4});
    ListNode* merged = mergeTwoLists(list1, list2);
    std::vector<int> result = listToVector(merged);
    assert(result == std::vector<int>({1, 1, 2, 3, 4, 4}));
    
    std::cout << "Problem 6: All tests passed!" << std::endl;
    return 0;
}
```

#### Problem 7: Best Time to Buy and Sell Stock
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Single pass with min tracking

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. Find the maximum profit you can achieve.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

int maxProfit(std::vector<int>& prices) {
    /*
    Find maximum profit from buying and selling stock once.
    
    Examples:
    Input: prices = [7,1,5,3,6,4]
    Output: 5 (buy at 1, sell at 6)
    
    Input: prices = [7,6,4,3,1]
    Output: 0 (no profit possible)
    */
    
    // Your code here
    return 0;
}

int main() {
    std::vector<int> prices1 = {7, 1, 5, 3, 6, 4};
    assert(maxProfit(prices1) == 5);
    
    std::vector<int> prices2 = {7, 6, 4, 3, 1};
    assert(maxProfit(prices2) == 0);
    
    std::vector<int> prices3 = {1, 2, 3, 4, 5};
    assert(maxProfit(prices3) == 4);
    
    std::cout << "Problem 7: All tests passed!" << std::endl;
    return 0;
}
```

### Day 7-8: Tree Basics

#### Problem 8: Maximum Depth of Binary Tree
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Tree traversal (DFS)

Given the `root` of a binary tree, return its maximum depth.

```cpp
#include <iostream>
#include <algorithm>
#include <cassert>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int maxDepth(TreeNode* root) {
    /*
    Find maximum depth of binary tree.
    
    Examples:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    
    Input: root = [1,null,2]
    Output: 2
    */
    
    // Your code here
    return 0;
}

int main() {
    // Create tree: [3,9,20,null,null,15,7]
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    
    assert(maxDepth(root) == 3);
    
    // Create tree: [1,null,2]
    TreeNode* root2 = new TreeNode(1);
    root2->right = new TreeNode(2);
    assert(maxDepth(root2) == 2);
    
    // Empty tree
    assert(maxDepth(nullptr) == 0);
    
    std::cout << "Problem 8: All tests passed!" << std::endl;
    return 0;
}
```

#### Problem 9: Same Tree
**Difficulty:** Easy  
**Time:** 15 minutes  
**Pattern:** Tree traversal comparison

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

```cpp
#include <iostream>
#include <cassert>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

bool isSameTree(TreeNode* p, TreeNode* q) {
    /*
    Check if two binary trees are identical.
    
    Examples:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    
    Input: p = [1,2], q = [1,null,2]
    Output: false
    */
    
    // Your code here
    return false;
}

int main() {
    // Create identical trees: [1,2,3]
    TreeNode* p1 = new TreeNode(1);
    p1->left = new TreeNode(2);
    p1->right = new TreeNode(3);
    
    TreeNode* q1 = new TreeNode(1);
    q1->left = new TreeNode(2);
    q1->right = new TreeNode(3);
    
    assert(isSameTree(p1, q1) == true);
    
    // Create different trees: [1,2] vs [1,null,2]
    TreeNode* p2 = new TreeNode(1);
    p2->left = new TreeNode(2);
    
    TreeNode* q2 = new TreeNode(1);
    q2->right = new TreeNode(2);
    
    assert(isSameTree(p2, q2) == false);
    
    std::cout << "Problem 9: All tests passed!" << std::endl;
    return 0;
}
```

### Day 9-10: Practice and Review

#### Problem 10: Contains Duplicate
**Difficulty:** Easy  
**Time:** 10 minutes  
**Pattern:** Hash set for uniqueness check

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

```cpp
#include <vector>
#include <unordered_set>
#include <iostream>
#include <cassert>

bool containsDuplicate(std::vector<int>& nums) {
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
```

## Tips for Practice

1. **Time yourself** - Try to complete each problem within the suggested time
2. **Think before coding** - Spend 2-3 minutes understanding the problem and planning your approach
3. **Handle edge cases** - Empty arrays, null pointers, single elements
4. **Test your code** - Compile and run test cases before checking solutions
5. **Learn from mistakes** - If stuck, try for 5 more minutes before looking at hints

## Compilation Instructions

To compile and run any problem:

```bash
g++ -std=c++17 -o solution problem.cpp
./solution
```

Or with debugging symbols:
```bash
g++ -std=c++17 -g -o solution problem.cpp
./solution
```

## Difficulty Progression
- Start with Easy problems (1-3, 5, 7, 10)
- Move to slightly more complex Easy problems (4, 6, 8-9)
- Master these patterns before moving to Medium problems

Good luck with your C++ practice!