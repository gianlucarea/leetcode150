# 274. H-Index

# Given an array of integers citations where citations[i] is the number of citations 
# a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h 
# such that the given researcher has published at least h papers that have each been cited at least h times.

from typing import List
import unittest

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0] * (n + 1)

        for cit in citations:
            if cit >= n:
                temp[n] += 1
            else:
                temp[cit] += 1

        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i
            
# Use counting sort logic to determine the H-index efficiently.
# For each citation count, cap it at n (since h-index can’t exceed total papers).
# Then, sum counts backward to find the highest h where total >= h.

class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.hIndex([3,0,6,1,5]), 3) 

    def test_case2(self):
        self.assertEqual(self.sol.hIndex([1,3,1]), 1)

    def test_case3(self):
        self.assertEqual(self.sol.hIndex([1]), 1)

    def test_case4(self):
        self.assertEqual(self.sol.hIndex([10,8,5,4,3]), 4)

if __name__ == "__main__":
    unittest.main()
