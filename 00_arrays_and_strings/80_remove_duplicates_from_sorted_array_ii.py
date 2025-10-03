# 80. Remove Duplicates from Sorted Array II

# Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element appears at most twice. 
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying 
# the input array in-place with O(1) extra memory.

from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        control = 1 

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if control < 2:
                    nums[k] = nums[i]
                    k += 1
                control += 1
            else:
                nums[k] = nums[i]
                k += 1
                control = 1

        return k
    
# The solution removes duplicates from a sorted array while allowing each element at most twice.
# It uses two pointers and a counter to track valid placements, 
# ensuring efficiency by modifying the array in-place and returning the new length.

class TestRemoveDuplicatesII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,1,2,2,3]
        k = self.sol.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1,1,2,2,3])

    def test_case2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        k = self.sol.removeDuplicates(nums)
        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0,0,1,1,2,3,3])

if __name__ == "__main__":
    unittest.main()
