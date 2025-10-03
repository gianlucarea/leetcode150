# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

from typing import List
import unittest

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

# My solution is preatty Simple from line 9 to 12 we adjust k if k is > than array length
# in line 13 we switch in place the array divided from 0 to k with k to end of array

class TestRotate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5,6,7]
        self.sol.rotate(nums, 3)
        self.assertEqual(nums, [5,6,7,1,2,3,4])

    def test_case2(self):
        nums = [-1,-100,3,99]
        self.sol.rotate(nums, 2)
        self.assertEqual(nums, [3,99,-1,-100])

    def test_case3(self):
        nums = [1,2,3]
        self.sol.rotate(nums, 4)  # larger than length
        self.assertEqual(nums, [3,1,2])


if __name__ == "__main__":
    unittest.main()
