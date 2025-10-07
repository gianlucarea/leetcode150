# 380. Insert Delete GetRandom O(1)

# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# 1. bool insert(int val) Inserts an item val into the set if not present. 
#    Returns true if the item was not present, false otherwise.
# 
# 2. bool remove(int val) Removes an item val from the set if present. 
#    Returns true if the item was present, false otherwise.
# 
# 3. int getRandom() Returns a random element from the current set of elements 
#    (it's guaranteed that at least one element exists when this method is called). 
#   Each element must have the same probability of being returned.
# 
# You must implement the functions of the class such that each function works in average O(1) time complexity.

import random
import unittest

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        last_val = self.values[-1]
        idx = self.index_map[val]
        self.values[idx] = last_val
        self.index_map[last_val] = idx
        self.values.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# Use a list for storing values (for random access)
# and a dictionary to keep track of each value’s index.
# This allows O(1) insertion, deletion, and random retrieval.
class TestRandomizedSet(unittest.TestCase):
    def test_operations(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.insert(1))
        self.assertTrue(rs.insert(2))

        self.assertIn(rs.getRandom(), [1, 2])

        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.remove(1))

        self.assertEqual(rs.values, [2])
        self.assertIn(rs.getRandom(), [2])

    def test_empty_random(self):
        rs = RandomizedSet()
        rs.insert(10)
        rs.remove(10)
        self.assertEqual(rs.values, [])

if __name__ == "__main__":
    unittest.main()

