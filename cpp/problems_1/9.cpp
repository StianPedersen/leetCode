// ####Problem 9 : Same Tree
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Tree traversal comparison
//
// Given the roots of two binary trees `p` and `q`, write a function to check if
// they are the same or not.
//
// Two binary trees are considered the same if they are structurally identical,
// and the nodes have the same value.
//
// **Constraints:**
// - The number of nodes in both trees is in the range [0, 100].
// - -10^4 <= Node.val <= 10^4
//
// **Hint:** Think about what makes two trees identical - they need to have the
// same structure AND the same values. Consider using recursion to compare
// corresponding nodes. What are the base cases? What happens when one tree
// is null but the other isn't?

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

bool isSameTree(TreeNode *p, TreeNode *q) {
  /*
  Check if two binary trees are identical.

  Examples:
  Input: p = [1,2,3], q = [1,2,3]
  Output: true

  Input: p = [1,2], q = [1,null,2]
  Output: false
  */
  if (!p && !q) {
    return true;
  }
  if ((!p || !q) || (p->val != q->val)) {
    return false;
  }

  if (p->val == q->val && isSameTree(p->left, q->left) &&
      isSameTree(p->right, q->right)) {
    return true;
  }
  return false;
}

int main() {
  // Test 1: Identical trees [1,2,3]
  TreeNode *p1 = new TreeNode(1);
  p1->left = new TreeNode(2);
  p1->right = new TreeNode(3);

  TreeNode *q1 = new TreeNode(1);
  q1->left = new TreeNode(2);
  q1->right = new TreeNode(3);

  assert(isSameTree(p1, q1) == true);
  // Test 2: Different structure [1,2] vs [1,null,2]
  TreeNode *p2 = new TreeNode(1);
  p2->left = new TreeNode(2);

  TreeNode *q2 = new TreeNode(1);
  q2->right = new TreeNode(2);

  assert(isSameTree(p2, q2) == false);

  // Test 3: Different values [1,2,1] vs [1,1,2]
  TreeNode *p3 = new TreeNode(1);
  p3->left = new TreeNode(2);
  p3->right = new TreeNode(1);

  TreeNode *q3 = new TreeNode(1);
  q3->left = new TreeNode(1);
  q3->right = new TreeNode(2);

  assert(isSameTree(p3, q3) == false);

  // Test 4: Both trees null
  assert(isSameTree(nullptr, nullptr) == true);

  // Test 5: One tree null, other not null
  TreeNode *p5 = new TreeNode(1);
  assert(isSameTree(p5, nullptr) == false);
  assert(isSameTree(nullptr, p5) == false);

  // Test 6: Single node trees with same value
  TreeNode *p6 = new TreeNode(5);
  TreeNode *q6 = new TreeNode(5);
  assert(isSameTree(p6, q6) == true);

  // Test 7: Single node trees with different values
  TreeNode *p7 = new TreeNode(3);
  TreeNode *q7 = new TreeNode(7);
  assert(isSameTree(p7, q7) == false);

  // Test 8: Deeper tree with identical structure and values
  TreeNode *p8 = new TreeNode(1);
  p8->left = new TreeNode(2);
  p8->right = new TreeNode(3);
  p8->left->left = new TreeNode(4);
  p8->left->right = new TreeNode(5);

  TreeNode *q8 = new TreeNode(1);
  q8->left = new TreeNode(2);
  q8->right = new TreeNode(3);
  q8->left->left = new TreeNode(4);
  q8->left->right = new TreeNode(5);

  assert(isSameTree(p8, q8) == true);

  // Test 9: Same structure but one missing leaf
  TreeNode *p9 = new TreeNode(1);
  p9->left = new TreeNode(2);
  p9->right = new TreeNode(3);
  p9->left->left = new TreeNode(4);

  TreeNode *q9 = new TreeNode(1);
  q9->left = new TreeNode(2);
  q9->right = new TreeNode(3);

  assert(isSameTree(p9, q9) == false);

  std::cout << "Problem 9: All tests passed!" << std::endl;
  return 0;
}
