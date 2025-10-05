# 121. Best time to buy and sell stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
# in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

import unittest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = 10000
        current_max_profit = 0

        for num in prices:
            if num < current_min:
                current_min = num
            if current_min < num:
                current_max_profit = max(current_max_profit, num - current_min)
        
        return current_max_profit

# For each price in the list, we check if it’s lower than the current minimum price.
# If so, we update the current minimum to this price    .
# Otherwise, we calculate the profit by selling at this price and update the maximum profit
# if this profit is greater than any previously recorded profit.

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.maxProfit([7,1,5,3,6,4]), 5)  # Buy at 1, sell at 6

    def test_case2(self):
        self.assertEqual(self.sol.maxProfit([7,6,4,3,1]), 0)  # No profit possible

    def test_case3(self):
        self.assertEqual(self.sol.maxProfit([1,2,3,4,5]), 4)  # Increasing prices

if __name__ == "__main__":
    unittest.main()
