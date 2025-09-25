// #### Problem 7: Best Time to Buy and Sell Stock
// **Difficulty:** Easy
// **Time:** 15 minutes
// **Pattern:** Single pass with min tracking
//
// You are given an array `prices` where `prices[i]` is the price of a given
// stock on the `i`th day. Find the maximum profit you can achieve.

#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

int maxProfit(std::vector<int> &prices) {
  /*
  Find maximum profit from buying and selling stock once.

  Examples:
  Input: prices = [7,1,5,3,6,4]
  Output: 5 (buy at 1, sell at 6)

  Input: prices = [7,6,4,3,1]
  Output: 0 (no profit possible)
  */
  int max_value = 0;
  // Your code here
  for (size_t i = 0; i < prices.size(); i++) {
    for (size_t j = 1; j < prices.size() - i; j++) {
      if (prices[i] - prices[i + j] < max_value &&
          prices[i] - prices[i + j] < 0) {
        max_value = prices[i] - prices[i + j];
      }
    }
  }
  return abs(max_value);
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
