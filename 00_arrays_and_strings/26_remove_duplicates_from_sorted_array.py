# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, 
# you need to do the following things:

# 1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were present 
#    in nums initially. The remaining elements of nums are not important as well as the size of nums.
# 2. Return k.


from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

### 
# Knowing that nums is sorted we just check if the previous number is not equal to the current, if so we move the position 
# of the new discovered number to position k and then we increment k. Now from 0 to k we are going to have all unique numbers.
# We return k which is the number of unique elements.

# Note -> we start from k = 1 because being sorted we need to check the first time if the second element is not equal to the 
# element in position 0. If it is we are going to move anyway a new number later on down the algorithm to position 1
### 

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,2]
        k = self.sol.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1,2])

    def test_case2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        k = self.sol.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0,1,2,3,4])


if __name__ == "__main__":
    unittest.main()
