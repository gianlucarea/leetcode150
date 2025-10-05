# 122. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can sell and buy the stock multiple times on the same day, 
# ensuring you never hold than one share of the stock.

# Find and return the maximum profit you can achieve.

from typing import List
import unittest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_min = 10000

        for num in prices:
            if num < current_min:
                current_min = num
            elif num > current_min:
                profit += num - current_min
                current_min = num 
        
        return profit

# For each price in the list, we check if it’s lower than the current minimum price.
# If it is, we treat it as a new buying opportunity and update the current minimum.
# If the price rises above the current minimum, we sell immediately to capture profit,
# add that profit to the total, and set the current price as the new buying point.

class TestMaxProfitII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.maxProfit([7,1,5,3,6,4]), 7)  # (1→5) + (3→6)

    def test_case2(self):
        self.assertEqual(self.sol.maxProfit([1,2,3,4,5]), 4)  # increasing: 4 total profit

    def test_case3(self):
        self.assertEqual(self.sol.maxProfit([7,6,4,3,1]), 0)  # decreasing: no profit

if __name__ == "__main__":
    unittest.main()
