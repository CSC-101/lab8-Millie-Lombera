import unittest
from group import groups_of_3

class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        t1 = groups_of_3([1,2,3,4,5,6,7,8,9])
        self.assertEqual(t1, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_groups_of_3_2(self):
        t2 = groups_of_3(([1,2,3,4,5,6,7,8]))
        self.assertEqual(t2, [[1, 2, 3], [4, 5, 6], [7, 8]])