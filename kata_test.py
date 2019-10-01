from unittest import TestCase

from kata import Kata

class KataTest(TestCase):
    def test_solver_function_empty_string(self):
        self.assertEqual(Kata().solver_function(""), [], "Cycle 1: Empty String")

    def test_solver_function_one_number(self):
        self.assertEqual(Kata().solver_function("1"), [1], "Cycle 2: One Number")

    def test_solver_function_two_numbers(self):
        self.assertEqual(Kata().solver_function("1,2"), [1, 2], "Cycle 3: Two Numbers")
