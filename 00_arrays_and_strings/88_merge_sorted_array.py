# 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

from typing import List
import unittest

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        m = m - 1
        n = n - 1
        
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1

### 
# Knowing that nums1 has the lenght of k = n + m, we confront nums1[m] and nums2[n] and put in position nums[i] k 
# the greatest value. At the end when n and m have been consumed we have a sorted array after merge
### 

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        self.sol.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_case2(self):
        nums1 = [1]
        nums2 = []
        self.sol.merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

    def test_case3(self):
        nums1 = [0]
        nums2 = [1]
        self.sol.merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

if __name__ == "__main__":
    unittest.main()
