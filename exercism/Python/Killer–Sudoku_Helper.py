import unittest
import itertools

"""
Time started: 08:12 pm
Time alloted : 1 hour
Functional Programming paradigm
"""


def combinations(target, size, exclude):
    # Generate a range of numbers from 1 to 9
    numbers = list(range(1, 10))
    for i in exclude:
        numbers.remove(i)

    # Invariant 1 : Check if the numbers variable is correct

    numbers.sort()
    result = list(itertools.combinations(numbers, size))

    filtered_result = list(filter(lambda x: sum(x) == target, result))

    filtered_result_list = list(map(list, filtered_result))

    return filtered_result_list


class KillerSudokuHelperTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(combinations(1, 1, []), [[1]])

    def test_2(self):
        self.assertEqual(combinations(2, 1, []), [[2]])

    def test_3(self):
        self.assertEqual(combinations(3, 1, []), [[3]])

    def test_4(self):
        self.assertEqual(combinations(4, 1, []), [[4]])

    def test_5(self):
        self.assertEqual(combinations(5, 1, []), [[5]])

    def test_6(self):
        self.assertEqual(combinations(6, 1, []), [[6]])

    def test_7(self):
        self.assertEqual(combinations(7, 1, []), [[7]])

    def test_8(self):
        self.assertEqual(combinations(8, 1, []), [[8]])

    def test_9(self):
        self.assertEqual(combinations(9, 1, []), [[9]])

    def test_cage_with_sum_45_contains_all_digits_1_9(self):
        self.assertEqual(combinations(45, 9, []), [[1, 2, 3, 4, 5, 6, 7, 8, 9]])

    def test_cage_with_only_1_possible_combination(self):
        self.assertEqual(combinations(7, 3, []), [[1, 2, 4]])

    def test_cage_with_several_combinations(self):
        self.assertEqual(combinations(10, 2, []), [[1, 9], [2, 8], [3, 7], [4, 6]])

    def test_cage_with_several_combinations_that_is_restricted(self):
        self.assertEqual(combinations(10, 2, [1, 4]), [[2, 8], [3, 7]])


test = KillerSudokuHelperTest()
test.test_cage_with_several_combinations_that_is_restricted()
