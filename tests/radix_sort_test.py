import unittest
from src.radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(radix_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802])

    def test_empty_array(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element(self):
        self.assertEqual(radix_sort([1]), [1])

    def test_reverse_sorted(self):
        self.assertEqual(radix_sort([9, 8, 7, 6, 5]), [5, 6, 7, 8, 9])

    def test_negative_integers(self):
        # Note: Radix Sort is designed for non-negative integers
        # This test case serves as a demonstration and the function should handle it gracefully
        self.assertEqual(radix_sort([3, -6, 8, -10, 1, 2, -1]), [-10, -6, -1, 1, 2, 3, 8])

if __name__ == '__main__':
    unittest.main()
