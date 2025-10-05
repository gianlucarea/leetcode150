# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index,
#  and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

from typing import List
import unittest

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
        return True
    
# Treat each element as the amount of "fuel" (jumps) available from that position.
# As we move forward, decrease fuel by 1 for each step.
# If the current jump length is greater than the remaining fuel, refuel to that value.
# If fuel ever drops below 0 before the end, we can’t reach the last index.
# If we finish the loop, reaching the end is possible.

class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        # Can reach the last index: 2 -> 3 -> 4
        self.assertTrue(self.sol.canJump([2,3,1,1,4]))

    def test_case2(self):
        # Cannot reach the last index: stuck at index 3 (value 0)
        self.assertFalse(self.sol.canJump([3,2,1,0,4]))

    def test_case3(self):
        # Single element (already at last index)
        self.assertTrue(self.sol.canJump([0]))


if __name__ == "__main__":
    unittest.main()
