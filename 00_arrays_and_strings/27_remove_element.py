#27. Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, 
# you need to do the following things:

# 1. Change the array nums such that the first k elements of nums contain the elements which 
#    are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# 2. Return k.

from typing import List
import unittest

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

### 
# Simply we traverse the array moving in position k the numbers that are not equal to the val incrementing k. 
# We return k which is the number of elements not equal to the val elem at the end of the algorithm
###

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,2,2,3]
        val = 3
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [2,2])

    def test_case2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0,0,1,3,4]) 

if __name__ == "__main__":
    unittest.main()
