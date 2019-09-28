import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests lists when list is none"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """test when max is first"""
        self.assertEqual(max_list_iter([3,1,1]), 3)
        """test when max is second"""
        self.assertEqual(max_list_iter([1,3,1]), 3)
        """test when max is third"""
        self.assertEqual(max_list_iter([1,1,3]), 3)
        """test when all int are equal"""
        self.assertEqual(max_list_iter([1,1,1]), 1)
        """test when there is only one int"""
        self.assertEqual(max_list_iter([1]), 1)

    def test_reverse_rec(self):
        """test to reverse list"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        """test with list of length one"""
        self.assertEqual(reverse_rec([1]),[1])
        """test with empty list"""
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search(self):
        """tests with list that has an odd length"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        """test when target is in the middle"""
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        """test when target is at the end"""
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )
        """test when target is first"""
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        """test for every other position"""
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2 )
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 8 )
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 9 )
        """test with list that has even length"""
        list_val = [0,1,2,3,4,7,8,9]
        """test when target is at the end"""
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 9 )
        """test when target is first"""
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        """test for every other position"""
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2 )
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 8 )



if __name__ == "__main__":
        unittest.main()
