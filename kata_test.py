from unittest import TestCase

from kata import Kata
from kata import maxmin
from kata import minlen
from kata import MaxMinLen


class KataTest(TestCase):
    def test_solver_function_empty_string(self):
        self.assertEqual(Kata().solver_function(""), [], "Cycle 1: Empty String")

    def test_solver_function_one_number(self):
        self.assertEqual(Kata().solver_function("1"), [1], "Cycle 2: One Number")

    def test_solver_function_two_numbers(self):
        self.assertEqual(Kata().solver_function("1,2"), [1, 2], "Cycle 3: Two Numbers")

    def test_solver_function_n_numbers(self):
        self.assertEqual(Kata().solver_function("1,2,3,4"), [1, 2, 3, 4], "Cycle 4: N Numbers")


class MaxMinTest(TestCase):
    def test_solver_function_empty_string_max(self):
        self.assertEqual(maxmin().solver_function_max(""), [], "Cycle 1: Empty String max")
    def test_solver_function_one_number_max(self):
        self.assertEqual(maxmin().solver_function_max("1"), [1], "Cycle 2: One Number max")
    def test_solver_function_two_numbers_max(self):
        self.assertEqual(maxmin().solver_function_max("1,2"), [2], "Cycle 3: Two Numbers max")
    def test_solver_function_N_numbers_max(self):
        self.assertEqual(maxmin().solver_function_max("1,2,3,4"), [4, 4], "Cycle 4: N Numbers max and lenght")


class MinLenTest(TestCase):
    def test_solver_function_empty_string_minlen(self):
        self.assertEqual(minlen().solver_function_minlen(""), [], "Cycle 1: Empty String min")

    def test_solver_function_one_num_minlen(self):
        self.assertEqual(minlen().solver_function_minlen("1"), [1, 1], "Cycle 2: One Num min")

    def test_solver_function_two_num_minlen(self):
        self.assertEqual(minlen().solver_function_minlen("1,3"), [2, 3], "Cycle 3: Two Num min")

    def test_solver_function_n_num_minlen(self):
        self.assertEqual(minlen().solver_function_minlen("1,3,5,7,9"), [5, 9], "Cycle 4: N Num min")


class MaxMinLenTest(TestCase):
    def test_solver_function_n_nums_maxminlen(self):
        self.assertEqual(minlen().solver_function_minlen("1,3,5,7,9,12,15"), [7, 15, 1], "Cycle 5 - joint: N Numbers maxminlen")

