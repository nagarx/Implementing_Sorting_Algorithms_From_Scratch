import unittest
from src.heap_sort import HeapSort

class TestHeapSortAdvanced(unittest.TestCase):

    def test_large_array(self):
        arr = list(range(1, 1001))
        arr.reverse()
        heap_sort = HeapSort(arr)
        self.assertEqual(heap_sort.sort(), list(range(1, 1001)))

    def test_array_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        heap_sort = HeapSort(arr)
        self.assertEqual(heap_sort.sort(), [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_already_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort = HeapSort(arr)
        self.assertEqual(heap_sort.sort(), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort = HeapSort(arr)
        self.assertEqual(heap_sort.sort(), [1, 2, 3, 4, 5])

    def test_single_element_array(self):
        arr = [1]
        heap_sort = HeapSort(arr)
        self.assertEqual(heap_sort.sort(), [1])

    def test_empty_array(self):
        arr = []
        heap_sort = HeapSort(arr)
        self.assertEqual(heap_sort.sort(), [])

if __name__ == "__main__":
    unittest.main()
