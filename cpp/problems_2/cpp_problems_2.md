# LeetCode C++ Easy Problems - Practice Set 2

## Week 2: Advanced Fundamentals

### Day 1-2: Advanced Array and String Operations

#### Problem 11: Move Zeroes

**Difficulty:** Easy
**Time:** 15 minutes
**Pattern:** Two pointers technique

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

```cpp
#include <vector>
#include <iostream>
#include <cassert>

void moveZeroes(std::vector<int>& nums) {
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
```

#### Problem 12: Reverse String

**Difficulty:** Easy
**Time:** 10 minutes
**Pattern:** Two pointers

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

```cpp
#include <vector>
#include <iostream>
#include <cassert>

void reverseString(std::vector<char>& s) {
    /*
    Reverse string in-place.

    Examples:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
    */

    // Your code here
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
```

#### Problem 13: Single Number

**Difficulty:** Easy
**Time:** 15 minutes
**Pattern:** Bit manipulation (XOR)

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

```cpp
#include <vector>
#include <iostream>
#include <cassert>

int singleNumber(std::vector<int>& nums) {
    /*
    Find the element that appears only once.

    Examples:
    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [4,1,2,1,2]
    Output: 4

    Input: nums = [1]
    Output: 1
    */

    // Your code here
    return 0;
}

int main() {
    std::vector<int> nums1 = {2, 2, 1};
    assert(singleNumber(nums1) == 1);

    std::vector<int> nums2 = {4, 1, 2, 1, 2};
    assert(singleNumber(nums2) == 4);

    std::vector<int> nums3 = {1};
    assert(singleNumber(nums3) == 1);

    std::cout << "Problem 13: All tests passed!" << std::endl;
    return 0;
}
```

### Day 3-4: Linked Lists

#### Problem 14: Reverse Linked List

**Difficulty:** Easy
**Time:** 15 minutes
**Pattern:** Linked list reversal with pointers

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

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

ListNode* reverseList(ListNode* head) {
    /*
    Reverse a singly linked list.

    Examples:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Input: head = [1,2]
    Output: [2,1]

    Input: head = []
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
    ListNode* list1 = createList({1, 2, 3, 4, 5});
    ListNode* reversed1 = reverseList(list1);
    assert(listToVector(reversed1) == std::vector<int>({5, 4, 3, 2, 1}));

    ListNode* list2 = createList({1, 2});
    ListNode* reversed2 = reverseList(list2);
    assert(listToVector(reversed2) == std::vector<int>({2, 1}));

    assert(reverseList(nullptr) == nullptr);

    std::cout << "Problem 14: All tests passed!" << std::endl;
    return 0;
}
```

#### Problem 15: Linked List Cycle

**Difficulty:** Easy
**Time:** 20 minutes
**Pattern:** Floyd's cycle detection (fast/slow pointers)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

```cpp
#include <iostream>
#include <cassert>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

bool hasCycle(ListNode *head) {
    /*
    Detect if linked list has a cycle.

    Examples:
    Input: head = [3,2,0,-4], pos = 1 (cycle at node with value 2)
    Output: true

    Input: head = [1,2], pos = 0 (cycle at node with value 1)
    Output: true

    Input: head = [1], pos = -1 (no cycle)
    Output: false
    */

    // Your code here
    return false;
}

int main() {
    // Test 1: Cycle exists at position 1
    ListNode* head1 = new ListNode(3);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(0);
    head1->next->next->next = new ListNode(-4);
    head1->next->next->next->next = head1->next; // Creates cycle
    assert(hasCycle(head1) == true);

    // Test 2: No cycle
    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);
    assert(hasCycle(head2) == false);

    // Test 3: Empty list
    assert(hasCycle(nullptr) == false);

    std::cout << "Problem 15: All tests passed!" << std::endl;
    return 0;
}
```

### Day 5-6: Tree Operations

#### Problem 16: Invert Binary Tree

**Difficulty:** Easy
**Time:** 15 minutes
**Pattern:** Tree traversal (DFS)

Given the `root` of a binary tree, invert the tree, and return its root.

```cpp
#include <iostream>
#include <cassert>
#include <vector>
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* invertTree(TreeNode* root) {
    /*
    Invert/flip a binary tree (mirror image).

    Examples:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Input: root = [2,1,3]
    Output: [2,3,1]

    Input: root = []
    Output: []
    */

    // Your code here
    return nullptr;
}

// Helper function to convert tree to level-order vector
std::vector<int> treeToVector(TreeNode* root) {
    std::vector<int> result;
    if (!root) return result;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        result.push_back(node->val);
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
    return result;
}

int main() {
    // Test 1: Standard tree
    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(7);
    root1->left->left = new TreeNode(1);
    root1->left->right = new TreeNode(3);
    root1->right->left = new TreeNode(6);
    root1->right->right = new TreeNode(9);

    TreeNode* inverted1 = invertTree(root1);
    assert(treeToVector(inverted1) == std::vector<int>({4, 7, 2, 9, 6, 3, 1}));

    // Test 2: Empty tree
    assert(invertTree(nullptr) == nullptr);

    std::cout << "Problem 16: All tests passed!" << std::endl;
    return 0;
}
```

#### Problem 17: Symmetric Tree

**Difficulty:** Easy
**Time:** 20 minutes
**Pattern:** Tree traversal comparison

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

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

bool isSymmetric(TreeNode* root) {
    /*
    Check if tree is symmetric (mirror image).

    Examples:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

    Input: root = [1,2,2,null,3,null,3]
    Output: false
    */

    // Your code here
    return false;
}

int main() {
    // Test 1: Symmetric tree [1,2,2,3,4,4,3]
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(2);
    root1->left->left = new TreeNode(3);
    root1->left->right = new TreeNode(4);
    root1->right->left = new TreeNode(4);
    root1->right->right = new TreeNode(3);
    assert(isSymmetric(root1) == true);

    // Test 2: Not symmetric [1,2,2,null,3,null,3]
    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->right = new TreeNode(2);
    root2->left->right = new TreeNode(3);
    root2->right->right = new TreeNode(3);
    assert(isSymmetric(root2) == false);

    std::cout << "Problem 17: All tests passed!" << std::endl;
    return 0;
}
```

### Day 7-8: Math and Logic

#### Problem 18: Fizz Buzz

**Difficulty:** Easy
**Time:** 10 minutes
**Pattern:** Modulo operations

Given an integer `n`, return a string array `answer` (1-indexed) where:
- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5
- `answer[i] == "Fizz"` if `i` is divisible by 3
- `answer[i] == "Buzz"` if `i` is divisible by 5
- `answer[i] == i` (as a string) if none of the above conditions are true

```cpp
#include <vector>
#include <string>
#include <iostream>
#include <cassert>

std::vector<std::string> fizzBuzz(int n) {
    /*
    Generate FizzBuzz sequence.

    Examples:
    Input: n = 3
    Output: ["1","2","Fizz"]

    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    */

    // Your code here
    return {};
}

int main() {
    assert(fizzBuzz(3) == std::vector<std::string>({"1", "2", "Fizz"}));
    assert(fizzBuzz(5) == std::vector<std::string>({"1", "2", "Fizz", "4", "Buzz"}));
    assert(fizzBuzz(15) == std::vector<std::string>({"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"}));

    std::cout << "Problem 18: All tests passed!" << std::endl;
    return 0;
}
```

#### Problem 19: Power of Three

**Difficulty:** Easy
**Time:** 15 minutes
**Pattern:** Mathematical properties

Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.

```cpp
#include <iostream>
#include <cassert>
#include <cmath>

bool isPowerOfThree(int n) {
    /*
    Check if number is a power of three.

    Examples:
    Input: n = 27
    Output: true (3^3 = 27)

    Input: n = 0
    Output: false

    Input: n = 9
    Output: true (3^2 = 9)

    Input: n = 45
    Output: false
    */

    // Your code here
    return false;
}

int main() {
    assert(isPowerOfThree(27) == true);
    assert(isPowerOfThree(0) == false);
    assert(isPowerOfThree(9) == true);
    assert(isPowerOfThree(45) == false);
    assert(isPowerOfThree(1) == true);  // 3^0 = 1
    assert(isPowerOfThree(-3) == false);

    std::cout << "Problem 19: All tests passed!" << std::endl;
    return 0;
}
```

### Day 9-10: Array Manipulations

#### Problem 20: Rotate Array

**Difficulty:** Easy
**Time:** 20 minutes
**Pattern:** Array reversal

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

```cpp
#include <vector>
#include <iostream>
#include <cassert>

void rotate(std::vector<int>& nums, int k) {
    /*
    Rotate array to the right by k steps.

    Examples:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    */

    // Your code here
}

int main() {
    std::vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    rotate(nums1, 3);
    assert(nums1 == std::vector<int>({5, 6, 7, 1, 2, 3, 4}));

    std::vector<int> nums2 = {-1, -100, 3, 99};
    rotate(nums2, 2);
    assert(nums2 == std::vector<int>({3, 99, -1, -100}));

    std::vector<int> nums3 = {1, 2};
    rotate(nums3, 3);
    assert(nums3 == std::vector<int>({2, 1}));

    std::cout << "Problem 20: All tests passed!" << std::endl;
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

- Start with easier problems (11-13, 18)
- Move to linked list problems (14-15)
- Progress to tree problems (16-17)
- Master array manipulations (19-20)

Good luck with your C++ practice!