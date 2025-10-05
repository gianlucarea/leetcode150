# 45. Jump Game II

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. 
# In other words, if you are at index i, you can jump to any index (i + j) where:
#   0 <= j <= nums[i] and
#   i + j < n

# Return the minimum number of jumps to reach index n - 1. 
# The test cases are generated such that you can reach index n - 1.

from typing import List
import unittest

class Solution:
    def jump(self, nums: List[int]) -> int:        
        jumps, farthest, end = 0 , 0 ,0 

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])

            if farthest >= (len(nums) - 1):
                jumps += 1
                break

            if i == end:
                jumps += 1
                end = farthest

        return jumps
    
# We track the farthest point reachable within the current number of jumps (current_end),
# and the farthest point reachable overall so far (farthest).
# Each time we reach current_end, we must "jump" to continue — incrementing the jump counter.
# This greedy approach ensures we always take the minimal number of jumps.

class TestJumpGameII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.jump([2,3,1,1,4]), 2)  

    def test_case2(self):
        self.assertEqual(self.sol.jump([2,3,0,1,4]), 2) 

    def test_case3(self):
        self.assertEqual(self.sol.jump([2,3,1]), 1)  

if __name__ == "__main__":
    unittest.main()