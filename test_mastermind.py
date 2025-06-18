import unittest
from master_Mind import get_feedback

class TestMastermind(unittest.TestCase):
    def test_perfect_guess(self):
        self.assertEqual(get_feedback(['1', '2', '3', '4'], ['1', '2', '3', '4']), (4, 0))

    def test_partial_guess(self):
        self.assertEqual(get_feedback(['1', '2', '3', '4'], ['4', '3', '2', '1']), (0, 4))

    def test_mixed_feedback(self):
        self.assertEqual(get_feedback(['1', '2', '3', '4'], ['1', '4', '2', '5']), (1, 2))

    def test_no_match(self):
        self.assertEqual(get_feedback(['1', '2', '3', '4'], ['5', '5', '5', '5']), (0, 0))

if __name__ == "__main__":
    unittest.main()
