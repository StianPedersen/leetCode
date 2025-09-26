// ####Problem 8 : Maximum Depth of Binary Tree **Difficulty : **Easy **Time
//     : **15 minutes **Pattern : **Tree traversal (DFS/BFS)
//
// **Description:**
// A binary tree's maximum depth is the number of nodes along the longest path
// from the root node down to the farthest leaf node. This can be solved using
// either depth-first search (DFS) recursively or breadth-first search (BFS)
// iteratively with a queue.
//
// **Approach:**
// 1. DFS (Recursive): For each node, recursively find the max depth of left
//    and right subtrees, then return 1 + max(leftDepth, rightDepth)
// 2. BFS (Iterative): Use level-order traversal with a queue, counting levels
//
// **Time Complexity:** O(n) where n is the number of nodes
// **Space Complexity:** O(h) where h is the height of the tree (recursion
// stack)
//
// Given the `root` of a binary tree, return its maximum depth.

#include <algorithm>
#include <cassert>
#include <iostream>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

int maxDepth(TreeNode *root) {
  /*
  Find maximum depth of binary tree.

  Examples:
  Input: root = [3,9,20,null,null,15,7]
  Output: 3

  Input: root = [1,null,2]
  Output: 2
  */
  if (root == nullptr) {
    return 0;
  }
  return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
}

int main() {
  // Test 1: Standard balanced tree [3,9,20,null,null,15,7]
  //         3
  //       /   \
  //      9     20
  //           /  \
  //         15    7
  TreeNode *root1 = new TreeNode(3);
  root1->left = new TreeNode(9);
  root1->right = new TreeNode(20);
  root1->right->left = new TreeNode(15);
  root1->right->right = new TreeNode(7);
  assert(maxDepth(root1) == 3);

  // Test 2: Right-skewed tree [1,null,2]
  //     1
  //      \
  //       2
  TreeNode *root2 = new TreeNode(1);
  root2->right = new TreeNode(2);
  assert(maxDepth(root2) == 2);

  // Test 3: Empty tree
  assert(maxDepth(nullptr) == 0);

  // Test 4: Single node tree
  TreeNode *root3 = new TreeNode(42);
  assert(maxDepth(root3) == 1);

  // Test 5: Left-skewed tree
  //       1
  //      /
  //     2
  //    /
  //   3
  //  /
  // 4
  TreeNode *root4 = new TreeNode(1);
  root4->left = new TreeNode(2);
  root4->left->left = new TreeNode(3);
  root4->left->left->left = new TreeNode(4);
  assert(maxDepth(root4) == 4);

  // Test 6: Perfect binary tree depth 3
  //         1
  //       /   \
  //      2     3
  //     / \   / \
  //    4   5 6   7
  TreeNode *root5 = new TreeNode(1);
  root5->left = new TreeNode(2);
  root5->right = new TreeNode(3);
  root5->left->left = new TreeNode(4);
  root5->left->right = new TreeNode(5);
  root5->right->left = new TreeNode(6);
  root5->right->right = new TreeNode(7);
  assert(maxDepth(root5) == 3);

  // Test 7: Unbalanced tree with different left/right depths
  //         1
  //       /   \
  //      2     3
  //     / \     \
  //    4   5     6
  //   /           \
  //  7             8
  //               /
  //              9
  TreeNode *root6 = new TreeNode(1);
  root6->left = new TreeNode(2);
  root6->right = new TreeNode(3);
  root6->left->left = new TreeNode(4);
  root6->left->right = new TreeNode(5);
  root6->right->right = new TreeNode(6);
  root6->left->left->left = new TreeNode(7);
  root6->right->right->right = new TreeNode(8);
  root6->right->right->right->left = new TreeNode(9);
  assert(maxDepth(root6) == 5);

  std::cout << "Problem 8: All tests passed!" << std::endl;
  return 0;
}
