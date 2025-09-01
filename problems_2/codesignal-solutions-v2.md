# CodeSignal Python Practice Solutions v2 - Advanced Patterns

## Matrix and 2D Array Problems

### Problem 1: Spiral Matrix Traversal - SOLUTION
**Pattern:** Matrix traversal with boundaries

```python
def spiral_order(matrix):
    """
    Traverse matrix in spiral order using boundary pointers.
    Move: right -> down -> left -> up, shrinking boundaries.
    """
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Move right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Move down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Move left along bottom row (if there is a row)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Move up along left column (if there is a column)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Alternative: Direction-based approach
def spiral_order_v2(matrix):
    """Using direction vectors"""
    if not matrix:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    visited = [[False] * n for _ in range(m)]
    
    # Direction vectors: right, down, left, up
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r = c = di = 0
    
    for _ in range(m * n):
        result.append(matrix[r][c])
        visited[r][c] = True
        
        # Try to continue in same direction
        nr, nc = r + dr[di], c + dc[di]
        
        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
            r, c = nr, nc
        else:
            # Change direction (turn right)
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    
    return result

# Test cases
assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert spiral_order([[1]]) == [1]
assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
print("Problem 1: All tests passed!")
```

### Problem 2: Rotate Matrix 90 Degrees - SOLUTION
**Pattern:** In-place matrix manipulation

```python
def rotate_matrix(matrix):
    """
    Rotate 90° clockwise = Transpose + Reverse each row
    Or: Rotate layer by layer from outside to inside
    """
    if not matrix:
        return matrix
    
    n = len(matrix)
    
    # Method 1: Transpose then reverse each row
    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

def rotate_matrix_v2(matrix):
    """
    Method 2: Rotate in layers/rings
    """
    n = len(matrix)
    
    # Process each layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Save top
            top = matrix[first][i]
            
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # top -> right
            matrix[i][last] = top
    
    return matrix

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

print("Problem 2: All tests passed!")
```

## Binary Search Variations

### Problem 3: Find Peak Element - SOLUTION
**Pattern:** Modified binary search

```python
def find_peak_element(nums):
    """
    Binary search: Move towards the higher neighbor.
    A peak must exist (nums[-1] = nums[n] = -∞).
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Compare with right neighbor
        if nums[mid] > nums[mid + 1]:
            # Peak is in left half (including mid)
            right = mid
        else:
            # Peak is in right half (excluding mid)
            left = mid + 1
    
    return left

def find_peak_element_v2(nums):
    """
    Linear scan approach (simpler but O(n))
    """
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1

# Test cases
assert find_peak_element([1, 2, 3, 1]) == 2
result = find_peak_element([1, 2, 1, 3, 5, 6, 4])
assert result in [1, 5]  # Both are valid peaks
assert find_peak_element([1]) == 0
assert find_peak_element([2, 1]) == 0
print("Problem 3: All tests passed!")
```

### Problem 4: Search in Rotated Array - SOLUTION
**Pattern:** Binary search with rotation

```python
def search_rotated(nums, target):
    """
    Binary search: Determine which half is sorted,
    then check if target is in that range.
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def search_rotated_v2(nums, target):
    """
    Alternative: Find pivot first, then binary search
    """
    def find_pivot(nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def binary_search(nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    if not nums:
        return -1
    
    pivot = find_pivot(nums)
    
    # Search in appropriate half
    if pivot == 0:
        return binary_search(nums, 0, len(nums) - 1, target)
    if target >= nums[0]:
        return binary_search(nums, 0, pivot - 1, target)
    return binary_search(nums, pivot, len(nums) - 1, target)

# Test cases
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated([1], 0) == -1
assert search_rotated([1], 1) == 0
assert search_rotated([3, 1], 1) == 1
print("Problem 4: All tests passed!")
```

## Linked List Problems

### Problem 5: Detect Cycle Start - SOLUTION
**Pattern:** Floyd's cycle detection

```python
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def detect_cycle_start(head):
    """
    Floyd's algorithm:
    1. Detect cycle using fast/slow pointers
    2. Find start by moving one pointer to head
    3. Move both one step at a time until they meet
    """
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if cycle exists
    slow = fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    
    if not has_cycle:
        return None
    
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def detect_cycle_start_v2(head):
    """
    Using set to track visited nodes (O(n) space)
    """
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next
    
    return None

# Test helper function
def create_cycle_list(values, pos):
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

print("Problem 5: All tests passed!")
```

### Problem 6: Reverse Nodes in k-Group - SOLUTION
**Pattern:** Linked list manipulation

```python
def reverse_k_group(head, k):
    """
    Reverse k nodes at a time.
    1. Check if k nodes available
    2. Reverse k nodes
    3. Connect with previous group
    4. Move to next group
    """
    def reverse_linked_list(head, k):
        """Reverse k nodes and return new head"""
        prev = None
        curr = head
        
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
    # Count total nodes
    count = 0
    node = head
    while node:
        count += 1
        node = node.next
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    
    while count >= k:
        group_start = prev_group.next
        group_end = group_start
        
        # Find end of current group
        for _ in range(k - 1):
            group_end = group_end.next
        
        # Save next group start
        next_group = group_end.next
        
        # Reverse current group
        group_end.next = None
        prev_group.next = reverse_linked_list(group_start, k)
        
        # Connect reversed group
        group_start.next = next_group
        
        # Move to next group
        prev_group = group_start
        count -= k
    
    return dummy.next

def reverse_k_group_v2(head, k):
    """
    Recursive approach
    """
    # Check if we have k nodes
    curr = head
    count = 0
    
    while curr and count < k:
        curr = curr.next
        count += 1
    
    if count < k:
        return head
    
    # Reverse first k nodes
    prev = None
    curr = head
    
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # Recursively reverse remaining groups
    if curr:
        head.next = reverse_k_group_v2(curr, k)
    
    return prev

# Helper functions
def list_to_linked(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

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

print("Problem 6: All tests passed!")
```

## Bit Manipulation

### Problem 7: Single Number (Find Unique) - SOLUTION
**Pattern:** XOR properties

```python
def single_number(nums):
    """
    XOR properties:
    - a ^ a = 0
    - a ^ 0 = a
    - XOR is commutative and associative
    
    All duplicates cancel out, leaving the single number.
    """
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_v2(nums):
    """
    Using reduce for more functional approach
    """
    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)

# Test cases
assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
assert single_number([3, 3, 7, 7, 10, 11, 11]) == 10
print("Problem 7: All tests passed!")
```

### Problem 8: Count Set Bits (Hamming Weight) - SOLUTION
**Pattern:** Bit counting

```python
def hamming_weight(n):
    """
    Brian Kernighan's algorithm:
    n & (n-1) removes the rightmost 1 bit
    Count how many times we can do this.
    """
    count = 0
    while n:
        n &= n - 1  # Remove rightmost 1
        count += 1
    return count

def hamming_weight_v2(n):
    """
    Simple approach: Check each bit
    """
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1  # Right shift
    return count

def hamming_weight_v3(n):
    """
    Python built-in
    """
    return bin(n).count('1')

# Test cases
assert hamming_weight(11) == 3
assert hamming_weight(128) == 1
assert hamming_weight(255) == 8
assert hamming_weight(0) == 0
assert hamming_weight(1) == 1
print("Problem 8: All tests passed!")
```

## Interval Problems

### Problem 9: Merge Overlapping Intervals - SOLUTION
**Pattern:** Interval merging

```python
def merge_intervals(intervals):
    """
    Sort by start time, then merge overlapping intervals.
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if intervals overlap
        if current[0] <= last[1]:
            # Merge by extending end time
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged

def merge_intervals_v2(intervals):
    """
    Alternative: Process start and end points separately
    """
    if not intervals:
        return []
    
    intervals.sort()
    result = []
    
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result

# Test cases
assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
assert merge_intervals([[1, 4]]) == [[1, 4]]
assert merge_intervals([]) == []
print("Problem 9: All tests passed!")
```

### Problem 10: Insert Interval - SOLUTION
**Pattern:** Interval manipulation

```python
def insert_interval(intervals, new_interval):
    """
    Three phases:
    1. Add intervals before new_interval
    2. Merge overlapping intervals with new_interval
    3. Add intervals after new_interval
    """
    result = []
    i = 0
    n = len(intervals)
    
    # Phase 1: Add all intervals that end before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Phase 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Phase 3: Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

def insert_interval_v2(intervals, new_interval):
    """
    Alternative: Insert then merge
    """
    # Find insertion position
    pos = 0
    for i, interval in enumerate(intervals):
        if interval[0] < new_interval[0]:
            pos = i + 1
    
    intervals.insert(pos, new_interval)
    
    # Now merge overlapping intervals
    return merge_intervals(intervals)

# Test cases
assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
assert insert_interval([], [5, 7]) == [[5, 7]]
assert insert_interval([[1, 5]], [2, 3]) == [[1, 5]]
print("Problem 10: All tests passed!")
```

## Tree Problems

### Problem 11: Binary Tree Level Order Traversal - SOLUTION
**Pattern:** BFS on tree

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    BFS using queue to process nodes level by level.
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

def level_order_v2(root):
    """
    Using collections.deque for better performance
    """
    from collections import deque
    
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

def level_order_v3(root):
    """
    Recursive DFS approach with level tracking
    """
    def dfs(node, level, result):
        if not node:
            return
        
        # Ensure we have a list for this level
        if len(result) == level:
            result.append([])
        
        result[level].append(node.val)
        
        dfs(node.left, level + 1, result)
        dfs(node.right, level + 1, result)
    
    result = []
    dfs(root, 0, result)
    return result

# Helper to build tree
def build_tree(values):
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

print("Problem 11: All tests passed!")
```

### Problem 12: Maximum Path Sum in Binary Tree - SOLUTION
**Pattern:** DFS with global tracking

```python
def max_path_sum(root):
    """
    For each node, calculate:
    1. Max path going through this node
    2. Max path ending at this node (to return to parent)
    
    Track global maximum throughout.
    """
    def max_gain(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Get max sum going down left and right
        left_gain = max(max_gain(node.left), 0)  # Ignore negative paths
        right_gain = max(max_gain(node.right), 0)
        
        # Max path through current node
        current_max = node.val + left_gain + right_gain
        
        # Update global maximum
        max_sum = max(max_sum, current_max)
        
        # Return max gain if we continue path through parent
        return node.val + max(left_gain, right_gain)
    
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

def max_path_sum_v2(root):
    """
    Alternative with class to avoid nonlocal
    """
    class Solution:
        def __init__(self):
            self.max_sum = float('-inf')
        
        def max_gain(self, node):
            if not node:
                return 0
            
            left = max(0, self.max_gain(node.left))
            right = max(0, self.max_gain(node.right))
            
            self.max_sum = max(self.max_sum, node.val + left + right)
            
            return node.val + max(left, right)
    
    sol = Solution()
    sol.max_gain(root)
    return sol.max_sum

# Test cases
tree1 = build_tree([-10, 9, 20, None, None, 15, 7])
assert max_path_sum(tree1) == 42

tree2 = build_tree([1, 2, 3])
assert max_path_sum(tree2) == 6

tree3 = build_tree([-3])
assert max_path_sum(tree3) == -3

tree4 = build_tree([2, -1])
assert max_path_sum(tree4) == 2

print("Problem 12: All tests passed!")
```

## Summary of Patterns and Complexities

| Problem | Pattern | Time Complexity | Space Complexity |
|---------|---------|----------------|------------------|
| 1. Spiral Matrix | Boundary traversal | O(m×n) | O(1) |
| 2. Rotate Matrix | In-place manipulation | O(n²) | O(1) |
| 3. Find Peak | Binary search variant | O(log n) | O(1) |
| 4. Rotated Search | Modified binary search | O(log n) | O(1) |
| 5. Cycle Start | Floyd's algorithm | O(n) | O(1) |
| 6. Reverse k-Group | Linked list manipulation | O(n) | O(1) |
| 7. Single Number | XOR properties | O(n) | O(1) |
| 8. Count Bits | Bit manipulation | O(log n) | O(1) |
| 9. Merge Intervals | Sorting + merging | O(n log n) | O(n) |
| 10. Insert Interval | Linear scan | O(n) | O(n) |
| 11. Level Order | BFS | O(n) | O(n) |
| 12. Max Path Sum | DFS with tracking | O(n) | O(h) |

## Key Takeaways

1. **Matrix Problems**: Use boundary pointers or direction vectors
2. **Binary Search Variants**: Identify the sorted portion and adjust search
3. **Linked Lists**: Master pointer manipulation and dummy nodes
4. **Bit Manipulation**: Remember XOR properties and bit tricks
5. **Intervals**: Sort first, then process linearly
6. **Trees**: Choose between BFS (level-wise) and DFS (path-wise)

These problems cover advanced patterns commonly seen in technical interviews!