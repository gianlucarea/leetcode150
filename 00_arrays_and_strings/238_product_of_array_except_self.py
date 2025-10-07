# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal 
# to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List
import unittest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # Left pass
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        # Right pass
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output

# Use two passes to build prefix (left) and suffix (right) products.
# 1. First pass: multiply each position by all elements to its left.
# 2. Second pass: multiply each position by all elements to its right.
class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.productExceptSelf([1,2,3,4]), [24,12,8,6])

    def test_case2(self):
        self.assertEqual(self.sol.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

    def test_case3(self):
        self.assertEqual(self.sol.productExceptSelf([2,3,4,5]), [60,40,30,24])

    def test_case4(self):
        self.assertEqual(self.sol.productExceptSelf([1,1,1,1]), [1,1,1,1])

    def test_case5(self):
        self.assertEqual(self.sol.productExceptSelf([10]), [1])  # only one element

if __name__ == "__main__":
    unittest.main()
