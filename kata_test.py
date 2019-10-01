from unittest import TestCase

from kata import Kata

class KataTest(TestCase):
    def test_solver_function(self):
        self.assertEqual(Kata().solver_function(""), [], "Cycle 1: Empty String")
