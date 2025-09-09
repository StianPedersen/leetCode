# LeetCode C++ Easy Problems - Solutions Set 1

## Week 1: Fundamental Patterns - Solutions

### Day 1-2: Array and Hash Map Basics

#### Problem 1: Two Sum - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
#include <vector>
#include <unordered_map>
#include <iostream>
#include <cassert>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> numMap;
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (numMap.find(complement) != numMap.end()) {
            return {numMap[complement], i};
        }
        numMap[nums[i]] = i;
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
    
    std::cout << "Problem 1: All tests passed!" << std::endl;
    return 0;
}
```

**Explanation:** Use a hash map to store each number and its index as we iterate. For each number, check if its complement (target - current number) exists in the map.

---

#### Problem 2: Valid Parentheses - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
#include <string>
#include <stack>
#include <iostream>
#include <cassert>

bool isValid(std::string s) {
    std::stack<char> stack;
    
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            stack.push(c);
        } else {
            if (stack.empty()) return false;
            
            char top = stack.top();
            stack.pop();
            
            if ((c == ')' && top != '(') ||
                (c == '}' && top != '{') ||
                (c == ']' && top != '[')) {
                return false;
            }
        }
    }
    
    return stack.empty();
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

**Explanation:** Use a stack to track opening brackets. For each closing bracket, check if it matches the most recent opening bracket. The string is valid if the stack is empty at the end.

---

#### Problem 3: Remove Duplicates from Sorted Array - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```cpp
#include <vector>
#include <iostream>
#include <cassert>

int removeDuplicates(std::vector<int>& nums) {
    if (nums.empty()) return 0;
    
    int writeIndex = 1;  // Position to write next unique element
    
    for (int readIndex = 1; readIndex < nums.size(); readIndex++) {
        if (nums[readIndex] != nums[readIndex - 1]) {
            nums[writeIndex] = nums[readIndex];
            writeIndex++;
        }
    }
    
    return writeIndex;
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

**Explanation:** Use two pointers - one for reading and one for writing. Since array is sorted, duplicates are adjacent. Only write when we find a new unique element.

---

### Day 3-4: String Operations

#### Problem 4: Valid Palindrome - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```cpp
#include <string>
#include <cctype>
#include <iostream>
#include <cassert>

bool isPalindrome(std::string s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters from left
        while (left < right && !std::isalnum(s[left])) {
            left++;
        }
        
        // Skip non-alphanumeric characters from right
        while (left < right && !std::isalnum(s[right])) {
            right--;
        }
        
        // Compare characters (case-insensitive)
        if (std::tolower(s[left]) != std::tolower(s[right])) {
            return false;
        }
        
        left++;
        right--;
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
```

**Explanation:** Use two pointers from both ends. Skip non-alphanumeric characters and compare characters in a case-insensitive manner.

---

#### Problem 5: First Unique Character - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1) - at most 26 characters

```cpp
#include <string>
#include <unordered_map>
#include <iostream>
#include <cassert>

int firstUniqChar(std::string s) {
    std::unordered_map<char, int> charCount;
    
    // Count frequency of each character
    for (char c : s) {
        charCount[c]++;
    }
    
    // Find first character with count 1
    for (int i = 0; i < s.length(); i++) {
        if (charCount[s[i]] == 1) {
            return i;
        }
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
```

**Explanation:** First pass counts frequency of each character. Second pass finds the first character with frequency 1.

---

### Day 5-6: Linked Lists and Arrays

#### Problem 6: Merge Two Sorted Lists - Solution
**Difficulty:** Easy  
**Time Complexity:** O(m + n)  
**Space Complexity:** O(1)

```cpp
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
    ListNode dummy(0);
    ListNode* current = &dummy;
    
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }
    
    // Attach remaining nodes
    current->next = list1 ? list1 : list2;
    
    return dummy.next;
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

**Explanation:** Use a dummy node to simplify the merge logic. Compare the heads of both lists and attach the smaller one to the result.

---

#### Problem 7: Best Time to Buy and Sell Stock - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```cpp
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

int maxProfit(std::vector<int>& prices) {
    if (prices.empty()) return 0;
    
    int minPrice = prices[0];
    int maxProfit = 0;
    
    for (int i = 1; i < prices.size(); i++) {
        // Update minimum price seen so far
        minPrice = std::min(minPrice, prices[i]);
        
        // Calculate profit if we sell today
        int profit = prices[i] - minPrice;
        
        // Update maximum profit
        maxProfit = std::max(maxProfit, profit);
    }
    
    return maxProfit;
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

**Explanation:** Track the minimum price seen so far and the maximum profit achievable. For each price, calculate profit if we sell today and update maximum profit.

---

### Day 7-8: Tree Basics

#### Problem 8: Maximum Depth of Binary Tree - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is height

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
    if (!root) return 0;
    
    int leftDepth = maxDepth(root->left);
    int rightDepth = maxDepth(root->right);
    
    return std::max(leftDepth, rightDepth) + 1;
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

**Explanation:** Recursively find the maximum depth of left and right subtrees, then add 1 for the current node.

---

#### Problem 9: Same Tree - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is height

```cpp
#include <iostream>
#include <cassert>

bool isSameTree(TreeNode* p, TreeNode* q) {
    // Both nodes are null
    if (!p && !q) return true;
    
    // One is null, other is not
    if (!p || !q) return false;
    
    // Both are not null, compare values and recurse
    return (p->val == q->val) && 
           isSameTree(p->left, q->left) && 
           isSameTree(p->right, q->right);
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

**Explanation:** Recursively compare nodes. Trees are same if both nodes are null, or both have same value and same left/right subtrees.

---

### Day 9-10: Practice and Review

#### Problem 10: Contains Duplicate - Solution
**Difficulty:** Easy  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
#include <vector>
#include <unordered_set>
#include <iostream>
#include <cassert>

bool containsDuplicate(std::vector<int>& nums) {
    std::unordered_set<int> seen;
    
    for (int num : nums) {
        if (seen.find(num) != seen.end()) {
            return true;  // Found duplicate
        }
        seen.insert(num);
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
```

**Explanation:** Use a hash set to track seen numbers. If we encounter a number already in the set, we found a duplicate.

---

## Alternative Solutions

### Problem 3: Remove Duplicates (Alternative - using std::unique)
```cpp
#include <vector>
#include <algorithm>

int removeDuplicatesSTL(std::vector<int>& nums) {
    auto it = std::unique(nums.begin(), nums.end());
    return std::distance(nums.begin(), it);
}
```

### Problem 10: Contains Duplicate (Alternative - using sorting)
```cpp
#include <vector>
#include <algorithm>

bool containsDuplicateSort(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i-1]) return true;
    }
    return false;
}
// Time: O(n log n), Space: O(1) - modifies input
```

## Key Patterns Summary

1. **Hash Map/Set**: Problems 1, 5, 10 - Use for O(1) lookup
2. **Two Pointers**: Problems 3, 4 - Efficient array/string processing
3. **Stack**: Problem 2 - Last-in-first-out matching
4. **Recursion**: Problems 8, 9 - Tree traversal
5. **Greedy**: Problem 7 - Optimal substructure
6. **Linked List**: Problem 6 - Pointer manipulation

## Memory Management Note
In a real interview or production code, remember to properly manage memory when working with linked lists and trees (use smart pointers or proper deletion). The examples above focus on algorithm logic rather than memory management.

## Compilation and Testing
To test any solution:
```bash
g++ -std=c++17 -o solution solution.cpp && ./solution
```

All solutions include comprehensive test cases that verify correctness and handle edge cases.