// ####Problem 6 : Merge Two Sorted Lists **Difficulty : **Easy **Time
//     : **20 minutes **Pattern
//     : **Two pointers on linked lists
//
//           You are given the heads of two sorted linked lists `list1` and
//           `list2`
//               .Merge the two lists into one sorted list.
//
#include <cassert>
#include <iostream>
#include <vector>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
  /*
  Merge two sorted linked lists.

  Examples:
  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4,4]

  Input: list1 = [], list2 = []
  Output: []
  */

  // Your code here
  ListNode dummy(0);
  ListNode *curr = &dummy;

  while (list1 && list2) {
    if (list1->val >= list2->val) {
      curr->next = new ListNode(list2->val);
      curr = curr->next;
      list2 = list2->next;
    } else {
      curr->next = new ListNode(list1->val);
      curr = curr->next;
      list1 = list1->next;
    }
  }

  curr->next = list1 ? list1 : list2;
  return dummy.next;
}

// Helper function to create list from vector
ListNode *createList(std::vector<int> vals) {
  ListNode dummy(0);
  ListNode *current = &dummy;
  for (int val : vals) {
    current->next = new ListNode(val);
    current = current->next;
  }
  return dummy.next;
}

// Helper function to convert list to vector
std::vector<int> listToVector(ListNode *head) {
  std::vector<int> result;
  while (head) {
    result.push_back(head->val);
    head = head->next;
  }
  return result;
}

int main() {
  ListNode *list1 = createList({1, 2, 4});
  ListNode *list2 = createList({1, 3, 4});
  ListNode *merged = mergeTwoLists(list1, list2);
  std::vector<int> result = listToVector(merged);
  for (auto e : result) {
    std::cout << e << std::endl;
  }
  std::cout << std::endl;
  assert(result == std::vector<int>({1, 1, 2, 3, 4, 4}));

  std::cout << "Problem 6: All tests passed!" << std::endl;
  return 0;
}
