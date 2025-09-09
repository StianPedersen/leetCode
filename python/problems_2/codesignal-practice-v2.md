# CodeSignal Python Practice Problems v2 - Advanced Patterns

## Matrix and 2D Array Problems

### Problem 1: Spiral Matrix Traversal
**Difficulty:** Medium  
**Time:** 20 minutes  
**Pattern:** Matrix traversal with boundaries

Given an m x n matrix, return all elements of the matrix in spiral order (clockwise from outside to center).

```python
def spiral_order(matrix):
    """
    Traverse matrix in spiral order.
    
    Examples:
    Input: [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    Input: [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    # Your code here
    pass

# Test cases
assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_order([[1]]) == [1]
assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
print("All tests passed!")
```

### Problem 2: Rotate Matrix 90 Degrees
**Difficulty:** Medium  
**Time:** 15 minutes  
**Pattern:** In-place matrix manipulation

Rotate an n x n matrix 90 degrees clockwise in-place (modify the original matrix).

```python
def rotate_matrix(matrix):
    """
    Rotate matrix 90 degrees clockwise in-place.
    
    Example:
    Input: [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
    After rotation: [[7, 4, 1],
                     [8, 5, 2],
                     [9, 6, 3]]
    
    Note: Modify the matrix in-place and return it.
    """
    # Your code here
    pass

# Test cases
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix1)
assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix2 = [[1, 2], [3, 4]]
rotate_matrix(matrix2)
assert matrix2 == [[3, 1], [4, 2]]

matrix3 = [[1]]
rotate_matrix(matrix3)
assert matrix3 == [[1]]

print("All tests passed!")
```

## Binary Search Variations

### Problem 3: Find Peak Element
**Difficulty:** Medium  
**Time:** 15 minutes  
**Pattern:** Modified binary search

Find a peak element in an array. A peak element is greater than its neighbors. Return any peak's index.

```python
def find_peak_element(nums):
    """
    Find a peak element's index.
    nums[i] != nums[i+1] for all valid i.
    
    Examples:
    Input: [1, 2, 3, 1]
    Output: 2 (index of element 3)
    
    Input: [1, 2, 1, 3, 5, 6, 4]
    Output: 1 or 5 (both 2 and 6 are peaks)
    
    Note: nums[-1] = nums[n] = -∞ (conceptually)
    """
    # Your code here
    pass

# Test cases
assert find_peak_element([1, 2, 3, 1]) == 2
result = find_peak_element([1, 2, 1, 3, 5, 6, 4])
assert result in [1, 5]  # Both are valid peaks
assert find_peak_element([1]) == 0
assert find_peak_element([2, 1]) == 0
print("All tests passed!")
```

### Problem 4: Search in Rotated Array
**Difficulty:** Medium  
**Time:** 20 minutes  
**Pattern:** Binary search with rotation

Search for a target in a sorted array that has been rotated at an unknown pivot.

```python
def search_rotated(nums, target):
    """
    Search in rotated sorted array.
    
    Examples:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4 (index of 0)
    
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1 (not found)
    
    Input: nums = [1], target = 0
    Output: -1
    """
    # Your code here
    pass

# Test cases
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated([1], 0) == -1
assert search_rotated([1], 1) == 0
assert search_rotated([3, 1], 1) == 1
print("All tests passed!")
```

## Linked List Problems

### Problem 5: Detect Cycle Start
**Difficulty:** Medium  
**Time:** 20 minutes  
**Pattern:** Floyd's cycle detection (fast/slow pointers)

Given a linked list, return the node where the cycle begins. Return None if no cycle.

```python
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def detect_cycle_start(head):
    """
    Find the start of cycle in linked list.
    
    Example:
    3 -> 2 -> 0 -> -4
         ^          |
         |__________|
    
    Output: Node with value 2 (where cycle starts)
    
    If no cycle, return None.
    """
    # Your code here
    pass

# Test helper function
def create_cycle_list(values, pos):
    """Helper to create linked list with cycle at position pos"""
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

# Test cases
head1 = create_cycle_list([3, 2, 0, -4], 1)
result1 = detect_cycle_start(head1)
assert result1 and result1.val == 2

head2 = create_cycle_list([1, 2], 0)
result2 = detect_cycle_start(head2)
assert result2 and result2.val == 1

head3 = create_cycle_list([1], -1)  # No cycle
assert detect_cycle_start(head3) is None

print("All tests passed!")
```

### Problem 6: Reverse Nodes in k-Group
**Difficulty:** Hard  
**Time:** 25 minutes  
**Pattern:** Linked list manipulation

Reverse nodes of a linked list k at a time. If remaining nodes < k, leave them as is.

```python
def reverse_k_group(head, k):
    """
    Reverse every k nodes in linked list.
    
    Example:
    Input: 1->2->3->4->5, k = 2
    Output: 2->1->4->3->5
    
    Input: 1->2->3->4->5, k = 3
    Output: 3->2->1->4->5
    """
    # Your code here
    pass

# Helper function to convert list to linked list
def list_to_linked(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
head1 = list_to_linked([1, 2, 3, 4, 5])
result1 = reverse_k_group(head1, 2)
assert linked_to_list(result1) == [2, 1, 4, 3, 5]

head2 = list_to_linked([1, 2, 3, 4, 5])
result2 = reverse_k_group(head2, 3)
assert linked_to_list(result2) == [3, 2, 1, 4, 5]

head3 = list_to_linked([1, 2, 3])
result3 = reverse_k_group(head3, 1)
assert linked_to_list(result3) == [1, 2, 3]

print("All tests passed!")
```

## Bit Manipulation

### Problem 7: Single Number (Find Unique)
**Difficulty:** Easy  
**Time:** 10 minutes  
**Pattern:** XOR properties

Find the element that appears only once while all others appear twice.

```python
def single_number(nums):
    """
    Find the single element (all others appear twice).
    
    Examples:
    Input: [2, 2, 1]
    Output: 1
    
    Input: [4, 1, 2, 1, 2]
    Output: 4
    
    Use O(1) space complexity.
    """
    # Your code here
    pass

# Test cases
assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
assert single_number([3, 3, 7, 7, 10, 11, 11]) == 10
print("All tests passed!")
```

### Problem 8: Count Set Bits (Hamming Weight)
**Difficulty:** Easy  
**Time:** 10 minutes  
**Pattern:** Bit counting

Count the number of 1's in the binary representation of a number.

```python
def hamming_weight(n):
    """
    Count number of 1 bits in binary representation.
    
    Examples:
    Input: 11 (binary: 1011)
    Output: 3
    
    Input: 128 (binary: 10000000)
    Output: 1
    
    Input: 255 (binary: 11111111)
    Output: 8
    """
    # Your code here
    pass

# Test cases
assert hamming_weight(11) == 3
assert hamming_weight(128) == 1
assert hamming_weight(255) == 8
assert hamming_weight(0) == 0
assert hamming_weight(1) == 1
print("All tests passed!")
```

## Interval Problems

### Problem 9: Merge Overlapping Intervals
**Difficulty:** Medium  
**Time:** 15 minutes  
**Pattern:** Interval merging

Given a list of intervals, merge all overlapping intervals.

```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Examples:
    Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]
    
    Input: [[1, 4], [4, 5]]
    Output: [[1, 5]]
    """
    # Your code here
    pass

# Test cases
assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
assert merge_intervals([[1, 4]]) == [[1, 4]]
assert merge_intervals([]) == []
print("All tests passed!")
```

### Problem 10: Insert Interval
**Difficulty:** Medium  
**Time:** 20 minutes  
**Pattern:** Interval manipulation

Insert a new interval into a sorted list of non-overlapping intervals and merge if necessary.

```python
def insert_interval(intervals, new_interval):
    """
    Insert new interval and merge if necessary.
    
    Examples:
    Input: intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
    Output: [[1, 5], [6, 9]]
    
    Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], 
           new_interval = [4, 8]
    Output: [[1, 2], [3, 10], [12, 16]]
    """
    # Your code here
    pass

# Test cases
assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert insert_interval([], [5, 7]) == [[5, 7]]
assert insert_interval([[1, 5]], [2, 3]) == [[1, 5]]
print("All tests passed!")
```

## Tree Problems

### Problem 11: Binary Tree Level Order Traversal
**Difficulty:** Medium  
**Time:** 15 minutes  
**Pattern:** BFS on tree

Return the level-order traversal of a binary tree (nodes grouped by level).

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    Get level order traversal of binary tree.
    
    Example:
        3
       / \
      9   20
         /  \
        15   7
    
    Output: [[3], [9, 20], [15, 7]]
    """
    # Your code here
    pass

# Helper to build tree
def build_tree(values):
    """Build tree from list in level order"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
tree1 = build_tree([3, 9, 20, None, None, 15, 7])
assert level_order(tree1) == [[3], [9, 20], [15, 7]]

tree2 = build_tree([1])
assert level_order(tree2) == [[1]]

tree3 = build_tree([])
assert level_order(tree3) == []

tree4 = build_tree([1, 2, 3, 4, 5])
assert level_order(tree4) == [[1], [2, 3], [4, 5]]

print("All tests passed!")
```

### Problem 12: Maximum Path Sum in Binary Tree
**Difficulty:** Hard  
**Time:** 25 minutes  
**Pattern:** DFS with global tracking

Find the maximum path sum in a binary tree. Path can start and end at any nodes.

```python
def max_path_sum(root):
    """
    Find maximum path sum in binary tree.
    Path can start and end at any nodes.
    
    Example:
       -10
       /  \
      9    20
          /  \
         15   7
    
    Maximum path: 15 -> 20 -> 7 = 42
    
    Example:
        1
       / \
      2   3
    
    Maximum path: 2 -> 1 -> 3 = 6
    """
    # Your code here
    pass

# Test cases
tree1 = build_tree([-10, 9, 20, None, None, 15, 7])
assert max_path_sum(tree1) == 42

tree2 = build_tree([1, 2, 3])
assert max_path_sum(tree2) == 6

tree3 = build_tree([-3])
assert max_path_sum(tree3) == -3

tree4 = build_tree([2, -1])
assert max_path_sum(tree4) == 2

print("All tests passed!")
```

## Practice Tips

### Difficulty Levels:
- **Easy:** Problems 7, 8
- **Medium:** Problems 1, 2, 3, 4, 5, 9, 10, 11
- **Hard:** Problems 6, 12

### Key Patterns Covered:
1. **Matrix Manipulation:** Spiral traversal, rotation
2. **Binary Search Variations:** Peak finding, rotated array search
3. **Linked List:** Cycle detection, k-group reversal
4. **Bit Manipulation:** XOR tricks, bit counting
5. **Intervals:** Merging, insertion
6. **Tree Traversal:** BFS (level order), DFS (path sum)

### Time Management:
- Spend 2-3 minutes understanding the problem
- 2-3 minutes planning your approach
- Remaining time for implementation
- Save 2 minutes for testing edge cases

Good luck with your practice!