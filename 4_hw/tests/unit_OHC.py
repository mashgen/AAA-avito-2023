import unittest

from one_hot_encoder import fit_transform

TEST_INPUT = ["My", "name", "is", "Maria", "it", "is", "usual", "name"]
EXPECTED_OUTPUT = [
    ("My", [0, 0, 0, 0, 0, 1]),
    ("name", [0, 0, 0, 0, 1, 0]),
    ("is", [0, 0, 0, 1, 0, 0]),
    ("Maria", [0, 0, 1, 0, 0, 0]),
    ("it", [0, 1, 0, 0, 0, 0]),
    ("is", [0, 0, 0, 1, 0, 0]),
    ("usual", [1, 0, 0, 0, 0, 0]),
    ("name", [0, 0, 0, 0, 1, 0]),
]


class TestOneHotEncoder(unittest.TestCase):
    def test_empty_input(self):
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_one_word(self):
        actual = fit_transform("test")
        expected = [("test", [1])]
        self.assertEqual(actual, expected)

    def test_multiple_words_as_list(self):
        self.assertListEqual(fit_transform(TEST_INPUT), EXPECTED_OUTPUT)

    def test_multiple_words_as_args(self):
        self.assertListEqual(fit_transform(*TEST_INPUT), EXPECTED_OUTPUT)

    def test_incorrect_input(self):
        with self.assertRaises(
            TypeError,
            msg="expected at least 1 arguments, got 0"
        ):
            fit_transform()
