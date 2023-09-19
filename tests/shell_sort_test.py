# Implementing a basic unit test for the shell_sort function.
import unittest
from src.shell_sort import shell_sort


class TestShellSort(unittest.TestCase):

    def test_sort(self):
        # Test with integer list
        self.assertEqual(shell_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

        # Test with empty list
        self.assertEqual(shell_sort([]), [])

        # Test with list containing repeated elements
        self.assertEqual(shell_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])

        # Test with list containing a single element
        self.assertEqual(shell_sort([42]), [42])


# Running the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestShellSort))