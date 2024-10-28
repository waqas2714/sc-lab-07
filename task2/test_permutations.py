import unittest
from permutations import generate_permutations, generate_permutations_non_recursive

class TestPermutations(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            generate_permutations("", True)

    def test_single_character(self):
        self.assertEqual(generate_permutations("a", True), ["a"])
        self.assertEqual(generate_permutations("a", False), ["a"])

    def test_two_characters(self):
        self.assertEqual(generate_permutations("ab", True), ["ab", "ba"])
        self.assertEqual(generate_permutations("aa", False), ["aa"])
        self.assertEqual(generate_permutations("aa", False), ["aa"])

    def test_three_characters(self):
        self.assertEqual(generate_permutations("abc", True), ["abc", "acb", "bac", "bca", "cab", "cba"])
        self.assertEqual(generate_permutations("aab", False), ["aab", "aba", "baa"])
        self.assertEqual(generate_permutations("aab", False), ["aab", "aba", "baa"])

    def test_non_recursive_permutations(self):
        self.assertEqual(generate_permutations_non_recursive("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"])
        self.assertEqual(generate_permutations_non_recursive("aab"), ["aab", "aba", "baa"])

if __name__ == "__main__":
    unittest.main()
