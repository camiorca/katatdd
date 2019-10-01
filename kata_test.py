from unittest import TestCase

from kata import Kata
from kata import maxmin

class KataTest(TestCase):
    def test_solver_function_empty_string(self):
        self.assertEqual(Kata().solver_function(""), [], "Cycle 1: Empty String")

    def test_solver_function_one_number(self):
        self.assertEqual(Kata().solver_function("1"), [1], "Cycle 2: One Number")

    def test_solver_function_two_numbers(self):
        self.assertEqual(Kata().solver_function("1,2"), [1, 2], "Cycle 3: Two Numbers")

    def test_solver_function_n_numbers(self):
        self.assertEqual(Kata().solver_function("1,2,3,4"), [1, 2, 3, 4], "Cycle 4: N Numbers")

class maxmintest(TestCase):
    def test_solver_function_empty_string_max(self):
        self.assertEqual(maxmin().solver_function_max(""), [], "Cycle 1: Empty String max")
    def test_solver_function_one_number_max(self):
        self.assertEqual(maxmin().solver_function_max("1"), [1], "Cycle 2: One Number max")
    def test_solver_function_two_numbers_max(self):
        self.assertEqual(maxmin().solver_function_max("1,2"), [2], "Cycle 3: Two Numbers max")
    def test_solver_function_N_numbers_max(self):
        self.assertEqual(maxmin().solver_function_max("1,2,3,4"), [4], "Cycle 4: N Numbers max")
    def test_solver_function_N_numbers_max_list_len(self):
        self.assertEqual(maxmin().solver_function_max("1,2,3,4"), [4, 4], "Cycle 4: N Numbers max")