import unittest
from src.merge_sort import merge_sort
class TestMergeSort(unittest.TestCase):

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        arr = [3, -1, 2, -2, 1]
        merge_sort(arr)
        self.assertEqual(arr, [-2, -1, 1, 2, 3])

    def test_duplicates(self):
        arr = [5, 1, 3, 3, 2]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 3, 5])


# Run the test suite
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMergeSort))