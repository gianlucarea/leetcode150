# 169. Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

import unittest
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for num in nums:
            if counter == 0:
                result = num
                counter = 1
            elif result == num:
                counter += 1
            else:
                counter -= 1
        return result

# Easy solution using Boyer–Moore Voting Algorithm but being sure the is always a majority element in array
# we do not add the algorithmic check for n/2 

class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.majorityElement([3,2,3]), 3)

    def test_case2(self):
        self.assertEqual(self.sol.majorityElement([2,2,1,1,1,2,2]), 2)

    def test_case3(self):
        self.assertEqual(self.sol.majorityElement([3,3,4]), 3)


if __name__ == "__main__":
    unittest.main()
